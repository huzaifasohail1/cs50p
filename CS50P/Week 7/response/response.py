from validators import email

def main():
    emailInput = input('What is your email address? '.strip())
    if email(emailInput) == True:
        print('Valid')
    else:
        print('Invalid')

if __name__ == '__main__':
    main()