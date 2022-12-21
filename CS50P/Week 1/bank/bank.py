greeting = input("Greetings: ")
greeting1 = greeting.lower()
greeting2 = greeting1.strip()
if "hello" in greeting2:
    print("$0")
elif "h" == greeting2[0]:
    print("$20")
else:
    print("$100")