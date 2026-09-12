#Create a function that takes a list of numbers and returns the average.
def avg(ls):
    y = sum(ls)/len(ls)
    return y

ls = []
elem = int(input("Digite o numero de elementos da sua lista: "))
for i in range(1, elem+1):
    n = float(input("Digite um numero: "))
    ls.append(n)
print(f"sua lista: {ls}")

#calling func
media = avg(ls)
print(f"a media de sua lista: {media:.2f}")