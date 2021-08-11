# here is your word
word = input()
print("".join([symbol for i, symbol in enumerate(list(word)) if (i + 1) % 2 == 0]))
