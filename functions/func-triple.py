#Create a function that prints the triple of a number
def trip(x):
    y = x*3
    return y
x = int(input("Digite um numero x: "))
y = trip(x)
print(f"triplo de x: {y}")