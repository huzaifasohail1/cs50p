def main():
    inp= input('Input: ')
    devowelised_text = shorten(inp)
    print('Output:', devowelised_text)

def shorten(w):
    # vowels = ['a','e','i','o','u','A','E','I','O','U']
    vowels = ['a','e','i','o','u',]
    for vowel in vowels:
        if vowel in w:
            w = w.replace(vowel, '')
    return w

if __name__ == "__main__":
    main()
