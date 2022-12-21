def main():
    user_input = input("Please enter a smiley or frowney face: ").strip()
    print(convert(user_input))


def convert(user_input):
    input1 = user_input.replace(":(", "🙁").replace(":)", "🙂")
    return input1


main()