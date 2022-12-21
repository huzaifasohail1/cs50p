months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December",
]


def main():
    while True:
        try:
            input1 = input("Date: ").strip()

            if " " in input1:
                month, day, year = input1.split(" ")
                if month.title() in months:
                    day = int(day.strip(","))
                    month = int(months.index(month)) + 1
                    if month <= 12 and day <= 31:
                        print(f"{year}-{month:02}-{day:02}")
                        break

            else:
                month, day, year = map(int, input1.split("/"))
                if month <= 12 and day <= 31:
                    print(f"{year}-{month:02}-{day:02}")
                    break

        except ValueError:
            continue

        except (EOFError, KeyboardInterrupt):
            print("", end="\n")
            quit()

        else:
            continue


main()