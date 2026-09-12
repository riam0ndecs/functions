#Create a function that reverses a vector:
vet = []
def reversevet(vet):
    vet_reverse = vet[::-1]
    return f"seu vetor invertido: {vet_reverse}"

while True:
    num = int(input("Digite um número para adicionar ao vetor (0 para sair): "))
    if num == 0:
        break
    vet.append(num)
print(f"seu vetor: {vet}")
print(reversevet(vet))