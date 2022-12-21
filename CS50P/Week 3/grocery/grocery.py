def main():
    grolist = []
    while True:
        try:
            item = input().strip().lower()
            grolist.append(item)
        except (EOFError, KeyError):
            l = sorted(set(grolist))
            for i in l:
                print(f"{grolist.count(i)} {i.upper()}")
            quit()


main()