price = 50
while price > 0:
    print("Amount Due: ", price)
    insert = int(input("Insert Coin: "))
    if insert == 25 or insert == 10 or insert == 5:
        price -= insert
        
change = abs(price)
print(change)
