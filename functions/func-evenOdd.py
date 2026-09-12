#Create a function that takes a number and returns whether it is even or odd.
def even_odd(n):
    if n % 2 == 0:
        print(f"{n} é par")
        return "fim"
    else:
        print(f"{n} é impar")
        return "fim"
n = int(input("Digite um numero: "))
print(even_odd(n))