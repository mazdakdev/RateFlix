import torch
import torch.nn as nn
import numpy as np
from . import utils
import pickle

is_cuda = torch.cuda.is_available()

if is_cuda:
    device = torch.device("cuda")
    
else:
    device = torch.device("cpu") 

class SentimentRNN(nn.Module):
    def __init__(
        self,
        no_layers,
        vocab_size,
        hidden_dim,
        output_dim,
        embedding_dim,
        drop_prob=0.5,
        bidirectional=False,
    ):
        super(SentimentRNN, self).__init__()

        self.output_dim = output_dim
        self.hidden_dim = hidden_dim
        self.no_layers = no_layers
        self.vocab_size = vocab_size

        # embedding and LSTM layers
        self.embedding = nn.Embedding(vocab_size, embedding_dim)

        # lstm
        self.lstm = nn.LSTM(
            input_size=embedding_dim,
            hidden_size=self.hidden_dim,
            num_layers=no_layers,
            batch_first=True,
        )

        # dropout layer
        self.dropout = nn.Dropout(0.3)

        # linear and sigmoid layer
        self.fc = nn.Linear(self.hidden_dim, self.output_dim)
        self.sig = nn.Sigmoid()

    def forward(self, x, hidden):
        batch_size = x.size(0)

        # embeddings and lstm_out
        embeds = self.embedding(x)
        lstm_out, hidden = self.lstm(embeds, hidden)

        lstm_out = lstm_out.contiguous().view(-1, self.hidden_dim)

        # dropout and fully connected layer
        out = self.dropout(lstm_out)
        out = self.fc(out)

        # sigmoid function
        sig_out = self.sig(out)

        # reshape to be batch_size first
        sig_out = sig_out.view(batch_size, -1)

        sig_out = sig_out[:, -1]  # get last batch of labels

        # return last sigmoid output and hidden state
        return sig_out, hidden

    def init_hidden(self, batch_size):
        # Create two new tensors with sizes n_layers x batch_size x hidden_dim,
        # initialized to zero, for hidden state and cell state of LSTM
        h0 = torch.zeros((self.no_layers, batch_size, self.hidden_dim)).to(device)
        c0 = torch.zeros((self.no_layers, batch_size, self.hidden_dim)).to(device)
        hidden = (h0, c0)
        return hidden

class CommentAnalyzer:
    def __init__(self, model_path, vocab_path, is_gpu=False):

        with open(vocab_path, "rb") as f:
            self.vocab = pickle.load(f)

        no_layers = 2
        vocab_size = len(self.vocab) + 1  # extra 1 for padding
        embedding_dim = 64
        hidden_dim = 256

        self.model = SentimentRNN(
            no_layers=no_layers,
            vocab_size=vocab_size,
            hidden_dim=hidden_dim,
            embedding_dim=embedding_dim,
            output_dim=1,
            drop_prob=0.5,
        )

        if is_gpu:
            self.model.load_state_dict(torch.load(model_path))

        else:
            self.model.load_state_dict(torch.load(model_path, map_location=torch.device('cpu')))      

        self.model.eval()


    def predict(self, text: str) -> float:
        """
        Method to predict texts score from external apps
        """

        word_seq = np.array(
            [
                self.vocab[utils.preprocess_string(word)]
                for word in text.split()
                if utils.preprocess_string(word) in self.vocab.keys()
            ]
        )

        word_seq = np.expand_dims(word_seq, axis=0)
        pad = torch.from_numpy(utils.padding_(word_seq, 500))
        inputs = pad.to(device)
        batch_size = 1
        h = self.model.init_hidden(batch_size)
        h = tuple([each.data for each in h])
        output, h = self.model(inputs, h)

        return output.item() * 5 # Converting to 0-5 scale