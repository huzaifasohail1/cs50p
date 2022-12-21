def main():
    greet= input('Greeting: ')
    fine = value(greet)
    print('$'+str(fine))

def value(greet1):

    greet1 = greet1.lower().strip()

    if 'hello' in greet1:
        return(0)
    elif 'h' in greet1[0]:
        return(20)
    else:
        return(10)


if __name__ == "__main__":
    main()