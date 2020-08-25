numeros = list(range(10))

for n in range(0,10):
    numeros[n] = int(input("Digite seu número:"))

for i in range(0,10):
    for j in range(0,i):
        if(numeros[i] > numeros[j]):
            aux = numeros[i]
            numeros[i] = numeros[j]
            numeros[j] = aux

for n in range(0,10):
    print(numeros[n])