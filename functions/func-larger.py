#Create a function that takes two numbers and returns the larger of them
def larger(a,b):
    if a > b:
        return a
    else:
        return b
a = int(input("Digite um numero 'a': "))
b = int(input("Digite um numero 'b': "))
comp = larger(a,b)
print(f"o maior numero é: {comp}")