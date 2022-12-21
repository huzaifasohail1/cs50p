expression = input("Expression: ")
x, y, z = expression.split(" ")
x1 = float(x)
z1 = float(z)
if y == "+":
    result = x1 + z1
elif y == "-":
    result = x1 - z1
elif y == "*":
    result = x1 * z1
elif y == "/":
    result = x1 / z1
else:
    result = "Error"

print(round(result, 1))

