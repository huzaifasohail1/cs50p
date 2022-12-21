def main():
    fraction= check_fraction()
    if fraction <= 0.01:
        print("E")
    elif fraction >= 0.99:
        print("F")
    else:
        print(f"{round(fraction*100)}%")

def check_fraction():
    while True:
        try:
            xy=input("Fraction: ")
            x,y=xy.split("/")
            if (int(x) or int(y)):
                if int(y)>=int(x):
                    if y!=0:
                        return int(x)/int(y)
        except ValueError:
            pass
        except ZeroDivisionError:
            pass

main()