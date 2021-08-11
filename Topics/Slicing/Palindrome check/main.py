# please work with the preset variable `word`
forward = word
backward = "".join(list(reversed(forward)))

if forward == backward:
    print("Yes")
else:
    print("No")
