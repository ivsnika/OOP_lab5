import re

class Sentence:
    def __init__(self, words_list=None):
        # Вимога: Конструктор з підтримкою копіювання
        if isinstance(words_list, Sentence):
            self.words = words_list.words[:]
        elif words_list is None:
            self.words = []
        elif isinstance(words_list, list):
            self.words = words_list
        else:
            self.words = [words_list]

    # Вимога: Докладна інформація про об'єкт
    def __str__(self):
        return f"Об'єкт Sentence [Слів: {len(self.words)}]: {' '.join(self.words)}"

    # ЦЕЙ МЕТОД ВИПРАВЛЯЄ ТВОЮ ПОМИЛКУ (TypeError: has no len)
    def __len__(self):
        return len(self.words)

    # Додаємо, щоб можна було звертатися по індексу: sentence[i]
    def __getitem__(self, index):
        return self.words[index]

    def __setitem__(self, index, value):
        self.words[index] = value

    # Оператори для 5-ї лаби
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

    # Ітератор для 6-ї лаби
    def __iter__(self):
        sorted_words = sorted(self.words, key=str.lower)
        return iter(sorted_words)