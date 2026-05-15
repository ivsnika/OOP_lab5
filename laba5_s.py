import re

class Sentence:
    def __init__(self, words_list=None):
        if words_list is None:
            self.words = []
        elif isinstance(words_list, list):
            self.words = words_list
        else:
            self.words = [words_list]

    def __len__(self):
        return len(self.words)

    def __getitem__(self, index):
        return self.words[index]

    def __setitem__(self, index, value):
        self.words[index] = value

    def __add__(self, other):
        if isinstance(other, Sentence):
            return Sentence(self.words + other.words)
        elif isinstance(other, str):
            return Sentence(self.words + [other])
        return NotImplemented

    def __sub__(self, other):
        if isinstance(other, Sentence):
            new_words = [w for w in self.words if w not in other.words]
            return Sentence(new_words)
        elif isinstance(other, str):
            new_words = [w for w in self.words if w != other]
            return Sentence(new_words)
        return NotImplemented

    def __contains__(self, word):
        return word in self.words

    def __str__(self):
        return " ".join(self.words)