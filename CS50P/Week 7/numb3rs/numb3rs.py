import sys

def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    try:
        n = ip.strip().split('.')
        if len(n) != 4:
            return False
        for n1 in n:
            if int(n1)<0 or int(n1)>255:
                return False
        return True
    except:
        return True



if __name__ == "__main__":
    main()