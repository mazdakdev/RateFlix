import numpy as np
import re

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