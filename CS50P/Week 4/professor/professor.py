import random

def main():

    lev = get_level()
    score = 0

    for _ in range(10):
        x = generate_integer(lev)
        y = generate_integer(lev)

        ans = str(x+y)
        res = 0

        for i in range(4):
            if i == 3:
                print(x, '+', y, '=', ans)
                break

            print(x, '+', y, '=', end=' ')
            res = input()
            if res!=ans:
                print('EEE')
            else:
                score+=1
                break

    print('Score: ', score)

def get_level():
    while True:
        try:
            lev = input('Level: ')
            if lev.isnumeric():
                lev = int(lev)
            else:
                raise Exception
            if 0 < lev and lev < 4:
                return lev
            else:
                raise Exception
        except:
            pass


def generate_integer(lev):
    if lev == 1:
        return random.randint(0,9)
    elif lev == 2:
        return random.randint(10,99)
    else:
        return random.randint(100,999)

if __name__ == "__main__":
    main()