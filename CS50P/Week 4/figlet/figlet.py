from pyfiglet import Figlet
figlet = Figlet()

import sys
import random

list = figlet.getFonts()

def main():

    #If no arguments passed

    if len(sys.argv) == 1:
        inp = input("Input: ")
        figlet.setFont(font=random.choice(list))
        print(figlet.renderText(inp))

    #If 2 arguments passed
    elif len(sys.argv) == 3:
        if str(sys.argv[1]) in ["-f", "--font"] and str(sys.argv[2]) in list:
            inp = input("Input: ")
            figlet.setFont(font=sys.argv[2])
            print(figlet.renderText(inp))
        else:
            sys.exit("Invalid usage")
    else:
        sys.exit("Invalid usage")
main()



