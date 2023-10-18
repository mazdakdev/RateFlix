import torch
import torch.nn as nn
import numpy as np
import re
import pickle

class SentimentRNN(nn.Module):
    def __init__(
        self,
        no_layers,
        vocab_size,
        hidden_dim,
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
        self.fc = nn.Linear(self.hidden_dim, output_dim)
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

with open("vocab.pkl", "rb") as f:
    vocab = pickle.load(f)

is_cuda = torch.cuda.is_available()

if is_cuda:
    device = torch.device("cuda")
    print("GPU is available")
else:
    device = torch.device("cpu")
    print("GPU not available, CPU used")

def preprocess_string(s):
    s = re.sub(r"[^\w\s]", "", s)
    s = re.sub(r"\s+", "", s)
    s = re.sub(r"\d", "", s)

    return s

def padding_(sentences, seq_len):
    features = np.zeros((len(sentences), seq_len), dtype=int)
    for ii, review in enumerate(sentences):
        if len(review) != 0:
            features[ii, -len(review) :] = np.array(review)[:seq_len]
    return features


no_layers = 2
vocab_size = len(vocab) + 1  # extra 1 for padding
embedding_dim = 64
output_dim = 1
hidden_dim = 256

model = SentimentRNN(
    no_layers=no_layers,
    vocab_size=vocab_size,
    hidden_dim=hidden_dim,
    embedding_dim=embedding_dim,
    drop_prob=0.5,
)

model.load_state_dict(torch.load("state_dict.pt", map_location=torch.device('cpu')))

model.eval()

def predict_text(text):
    word_seq = np.array(
        [
            vocab[preprocess_string(word)]
            for word in text.split()
            if preprocess_string(word) in vocab.keys()
        ]
    )
    word_seq = np.expand_dims(word_seq, axis=0)
    pad = torch.from_numpy(padding_(word_seq, 500))
    inputs = pad.to(device)
    batch_size = 1
    h = model.init_hidden(batch_size)
    h = tuple([each.data for each in h])
    output, h = model(inputs, h)
    return output.item()*5

print(predict_text("Awesome"))


#TODO: OOP