def main():
    sentence = input("Enter your sentence: ")
    final = convert(sentence)
    print(final)


def convert(sentence):
    text1 = sentence.replace(":)","🙂")
    sentence = text1.replace(":(","🙁")
    return(sentence)


main()



