# Ex. 1

soma = 0

var1 = int(input("Digite um número: "))

while var1 > 0:
    soma += var1
    print(f"a soma é: {soma}")

    var1 = int(input("Digite um número: "))

# Ex. 2

soma = 0
num = 3

while num <=5:
    soma += num
    num += 1
    print(f"A soma será: {soma}")

# Ex. 3

num1 = int(input("Insira um número: "))

fatorial = 1
i = 1

while i <= num1:
    fatorial *= i
    i += 1
    print(f"fatorial é {fatorial}")

# Ex. 4 - inserir estrutura de condição dentro do while

realizado = False

while not realizado:
    entrada = int(input("Insira alguma coisa: "))
    
    if entrada == 999:
        realizado = True
    else:
        print(entrada)

# Ex. 5

lista = []
i = 0

while len(lista) <11:
    lista.append(i)
    i += 1
    print(lista)

# Ex. 6 - Encontrando a soma dos números em uma lista usando while

lista2 = [23, 45, 12, 10, 25]
soma = 0
i = 0

while i < len(lista2):
    soma += lista2[i]
    i += 1
    print(soma)


# Ex. 7 - Crie um programa que solicite 5 nomes e coloque eles numa lista.

listaNomes = []
i = 1

while i <= 5:
    nome = input("Digite seu nome: ")
    listaNomes.append(nome)
    i += 1
    print(listaNomes)

# Ex. 8 - Crie um programa que acumule 5 números inteiros e decremente os valores inseridos pelo usuário.

listaNum = []
i = 1
sub = 0

while i <= 5:
    numero = int(input('Digite um número: '))
    listaNum.append(numero)
    sub -= listaNum[i]
    i += 1
    print(sub)

# Ex. 9 - Crie um programa para gerar uma taboada, a partir de duas variáveis (número e limite).

inicio = int(input("Digite um número inicial: "))
limite = int(input("Digite um limite: "))
i = 1
valor = 0

while i < limite:
    valor = inicio * i
    print(f"{inicio} X {i} = {valor}")
    i += 1

# Ex. 10 - A partir de var word = 'engenharia de software'. Se o índice da word == 'e' or 'o', continue.

frase = "engenharia de software"
i = 0
listaLetras = []

while i < len(frase):
    list = frase[i]
    if list == "e" or list == "o":
        i += 1
        continue
    listaLetras.append(list)
    print(list)
    i += 1
print(listaLetras)
