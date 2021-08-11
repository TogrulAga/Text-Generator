from collections import Counter
from random import choice, choices
import nltk


class TextGenerator:
    def __init__(self):
        self.file = None
        self.get_file()
        self.tokenized_file = None
        self.bigrams = None
        self.heads_tails_dict = dict()
        self.first_word = None
        self.tokenize_file()
        self.calc_bigram_stats()
        self.make_bigram_dict()
        self.generate_text()

    def get_file(self):
        filename = input()

        with open(filename, "r", encoding="utf-8") as file:
            self.file = file.read()

    def tokenize_file(self):
        self.tokenized_file = self.file.split()

    def print_token_stats(self):
        n_all_tokens = len(self.tokenized_file)
        n_unique_tokens = len(Counter(self.tokenized_file))

        print("Corpus statistics")
        print(f"All tokens: {n_all_tokens}")
        print(f"Unique tokens: {n_unique_tokens}\n")

    def count_tokens(self):
        while True:
            try:
                index = input()

                if index == "exit":
                    break

                print(self.tokenized_file[int(index)])
            except (TypeError, ValueError):
                print("Type Error. Please input an integer.")
            except IndexError:
                print("Index Error. Please input an integer that is in the range of the corpus.")

    def calc_bigram_stats(self):
        bigrams = list(nltk.trigrams(self.tokenized_file))
        self.bigrams = list(map(lambda x: (x[0] + " " + x[1], x[2]), bigrams))

    def count_bigrams(self):
        print(f"Number of bigrams: {len(self.bigrams)}")

        while True:
            try:
                index = input()

                if index == "exit":
                    break

                print(f"Head: {self.bigrams[int(index)][0]}\tTail: {self.bigrams[int(index)][1]}")
            except (TypeError, ValueError):
                print("Type Error. Please input an integer.")
            except IndexError:
                print("Index Error. Please input an integer that is in the range of the corpus.")

    def make_bigram_dict(self):
        for head, tail in self.bigrams:
            tempt_dict = dict()
            self.heads_tails_dict.setdefault(head, tempt_dict)
            self.heads_tails_dict[head].update({tail: 1 if tail not in self.heads_tails_dict[head] else self.heads_tails_dict[head][tail] + 1})

    def count_tails(self):
        while True:
            try:
                head = input()

                if head == "exit":
                    break

                print(f"Head: {head}")

                if self.heads_tails_dict.setdefault(head, {}) == {}:
                    raise KeyError

                tails = self.heads_tails_dict[head]

                for tail, count in tails.items():
                    print(f"Tail: {tail}\tCount: {count}")

                print()
            except KeyError:
                print("The requested word is not in the model. Please input another word.")

    def generate_text(self):
        heads = list(map(lambda x: x[0], self.bigrams))
        possible_first_heads = list(filter(lambda x: x[0].isupper() and all(symbol not in ".?!" for symbol in x), heads))

        n_sentences = 0
        while True:
            if n_sentences == 10:
                break
            current_head = choice(possible_first_heads)
            sentence = current_head + " "
            n_words = 2
            while True:
                tails = [tail for tail, _ in self.heads_tails_dict[current_head].items()]
                weights = [weight for _, weight in self.heads_tails_dict[current_head].items()]
                tail = choices(tails, weights)[0]
                if tail[-1] in ".?!" and n_words <= 4:
                    break
                if tail[-1] in ".?!" and n_words >= 5:
                    sentence += tail + " "
                    print(sentence)
                    n_sentences += 1
                    n_words += 1
                    break
                elif tail[-1] not in ".?!":
                    sentence += tail + " "
                    n_words += 1
                    current_head = current_head.split()[-1] + " " + tail
                    continue


_ = TextGenerator()
