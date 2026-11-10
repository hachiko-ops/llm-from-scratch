
import re

class SimpleTokenizerV1:

    def __init__(self, vocab:dict):
        self.vocab = vocab
        self.inv_vocab = {v: k for k, v in vocab.items()}

    def encode(self, text:str):
        tokens = re.split(r'[,.:;?_!"()\']|--|\s', text)
        tokens = [item for item in tokens if item.strip()] # Remove empty tokens
        token_ids = [self.vocab[token] for token in tokens if token in self.vocab]
        return token_ids

    def decode(self, token_ids:list):
        text = ' '.join([self.inv_vocab[token_id] for token_id in token_ids if token_id in self.inv_vocab])
        text = re.sub(r'\s([,.:;?_!"()\'])', r'\1', text) # Remove space before punctuation
        return text