sentence = input("Input: ")
for letter in sentence:
    if not letter in ["a", "e", "i", "o", "u", "O"]:
        print(letter, end="")
print()


