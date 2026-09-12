#Create a function that returns the largest element in a vector.
vet = []
while True:
    num = int(input("Digite um número para adicionar ao vetor (0 para sair): "))
    if num == 0:
        break
    vet.append(num)
print(f"seu vetor: {vet}")
tam = len(vet)

def finder(vet):
    maior = vet[0]
    for i in range(tam):
        if vet[i] > maior:
            maior = vet[i]
        else:
            continue
    return f"maior numero do vetor: {maior}"

print(finder(vet))