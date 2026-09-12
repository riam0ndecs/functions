#Create a function that returns the sum of three variables.
def soma(x,y,z):
    s = x + y + z
    return s
a = int(input("Digite um numero 'a': "))
b = int(input("Digite um numero 'b': "))
c = int(input("Digite um numero 'c': "))
s = soma(a,b,c)
print(s)