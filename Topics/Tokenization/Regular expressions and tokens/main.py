from nltk.tokenize import regexp_tokenize


print(regexp_tokenize(pattern=r"[A-z'-]+", text=input()))
