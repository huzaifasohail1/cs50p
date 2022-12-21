def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    no_dollars = d.replace('$','')
    return float(no_dollars)


def percent_to_float(p):
    no_percent = p.replace('%','')
    finalp = float(no_percent) / 100
    return float(finalp)



main()