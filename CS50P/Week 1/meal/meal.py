def main():
    answer = input("Time: ")
    time = convert(answer)
    if time >= 7 and time <= 8:
        print("Breakfast Time")
    elif time >= 12 and time <= 13:
        print("lunch time")
    elif time >= 18 and time <= 19:
        print("dinner time")

def convert(time):
    h, m = time.split(":")
    mm = float(m) / int(60)
    return float(h) + mm


if __name__ == "__main__":
    main()