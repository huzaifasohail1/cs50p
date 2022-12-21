import inflect

def main():
    i = inflect.engine()
    list = []



    while True:
        try:

            inp = input("Name: ")
            #Add name to list
            list.append(inp)
            #Session ends when ctrl d happens

        except (EOFError, KeyError):
            print("Adieu, adieu, to " + i.join(list), end="\n")
            quit()
main()