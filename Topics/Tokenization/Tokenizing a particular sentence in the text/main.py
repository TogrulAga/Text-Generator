from nltk.tokenize import regexp_tokenize, sent_tokenize


string = input()
index = int(input())

print(regexp_tokenize(pattern="[A-z']+", text=sent_tokenize(string)[index]))
