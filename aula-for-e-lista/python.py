#While e for

lista = []

for i in range(5):
    nome = input("Digite seu nome: ")
    lista.append(nome)
    print(lista)

# Exemplo 2
soma = 0

for numero in range(1,4):
    soma += numero
    print(soma)

# Exemplo 3

subtracao = 0

for num in range(1,5):
    subtracao -= num
    print(subtracao)

# Exemplo 4

listaNomes = ['Ana', 'Laura', 'Pedro','Jose']

for j in listaNomes:
    print(j)


# Soletrando
nome = "gui"
for letras in nome:
    print(letras)

# Exemplo 5

nume =[1 ,2 ,3 ,4 ,5 ,6 ,7, 8]

maior = nume[0]

for k in nume:
    if k > maior:
        maior = k
print(f"O maior número é {maior}")

# Exemplo 6

listaNomes2 = ['Ana', 'Laura', 'Pedro', 'Jose', 1, 2, 3]

for c in listaNomes2:
    if c == "Pedro":
        continue
    print(c)


# Exemplo 7 - continue

for h in range(1,5):
    if h == 3:
        continue
    print(h)

# Exemplo 8 - Break

for m in range(1,5):
    if m == 3:
        break
    print(m)

# Atividade 1 - Calcule a soma dos números de 1 a 100.

soma2 = 0

for v in range(1,101):
    soma2 += v

print(soma2)

# Atividade 2 - Crie um programa que imprima quais são os números pares de 1 a 50 e calcule a soma dos valores pares.

for pares in range(1,51):
    if pares %2 == 0:
        print(pares)

# Atividade 3 - Escreva um programa que identifique quais valores são ímpares em uma rande de 1 a 51 e calcule a média destes valores.

somaImpar = 0
listaImpar= []

for impar in range(1,51):
    if impar %2 != 0:
        listaImpar.append(impar)
        print(impar)

    somaImpar += impar
    mediaImpar = somaImpar/len(listaImpar)
print(somaImpar)
print(mediaImpar)