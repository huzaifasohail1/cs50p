from datetime import date
import inflect
import sys
import re

def main():
    inpt=input('Date of Birth: ')
    print(get_min(inpt))


def get_min(inpt):

    if search := re.search(r'^(\d{4})-(\d{2})-(\d{2})$',inpt):
        inpt=list(search.groups())
    else:
        sys.exit('Invalid date')

    user_birthday = convert_bday(inpt)

    today = date.today()

    bday = date(user_birthday[0], user_birthday[1], user_birthday[2])

    diff = bday - today
    days_number = -int(diff.days)

    minutes = days_number * 24 * 60

    inf = inflect.engine()
    min_words = inf.number_to_words(minutes)

    min_words = min_words.replace(' and','').capitalize()

    return min_words + ' minutes'

def convert_bday(day):
    day = list(map(int, day))

    if day[1] < 0 or day[1] > 12:
        sys.exit('Invalid date')

    elif day[2] < 0 or day[2] > 31:
        sys.exit('Invalid date')

    return day



if __name__ == "__main__":
    main()