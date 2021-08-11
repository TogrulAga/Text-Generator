from nltk.tokenize import WordPunctTokenizer


word_punctuation = WordPunctTokenizer()

print(word_punctuation.tokenize(text=input()))
