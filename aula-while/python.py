# Ex. 1

soma = 0
lista_resultados = []

var1 = int(input("Digite um número: "))

while var1 != 0:
    soma += var1
    if var1 < 0:
        print(f"{soma - var1} + ({var1}) = {soma}")
    if var1 > 0:
        print(f"{soma - var1} + {var1} = {soma}")
    lista_resultados.append(soma)

    var1=int(input("Digite um número: "))
print(f"Os resultados foram: {lista_resultados}")

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

while i < limite + 1:
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

# Ex. 11 - Cadastro de alunos: Crie m algoritmo que solicite 3 nomes e 3 idades. Deixe a informação em uma lista no formato nome-idade

listaAlunos = []
listaIdade = []
i = 0

while i < 3:
    nomeAluno = input("Digite um nome:")
    idadeAluno = str(input("Digite a idade: "))
    listaAlunos.append(nomeAluno)
    listaIdade.append(idadeAluno)
    print(f"Aluno: {listaAlunos[i]}. Idade: {listaIdade[i]}")
    i += 1

# Ex. 12 - Crie uma estrutura ue solicite itens de compra de forma que só sejá possível sair da estrutura de repetição, caso o usuário digite sair. Coloque os itens em uma lista.

# lista_itens = []
# sair = False

# while not sair:
#     itens = input("O que deseja?: ")

#     if itens == "sair":
#         sair = True
#         continue
#     lista_itens.append(itens)
# print(lista_itens)

# Outra maneira

l = []

while True:
    i = input("Digite o que você deseja: ")
    if i == "sair":
        break
    l.append(i)
print(l)

# Ex. 13 - Crie um programa que solicite 5 números inteiros, armazene em uma lista o seu valor ao quadrado [numero, numero ** 2]

lista_numero = []
lista_quadrado = []
i = 0

while i < 5:
    num_escolhido = int(input("Digite um número: "))
    num_quadrado = num_escolhido ** 2
    lista_numero.append(num_escolhido)
    lista_quadrado.append(num_quadrado)
    print(f"Número escolhido: {lista_numero[i]} - O mesmo ao quadrado: {lista_quadrado[i]}")
    i += 1
print(f"lista dos números escolhidos: {lista_numero}")
print(f"lista dos números ao quadrado: {lista_quadrado}")

# Ex. 14 - Crie um programa que solicite nome, curso e idade de 3 pessoas, armazene cada pessoa como uma lista dentro de uma lista_completa.

lista_completa = []
i = 0

while i < 3:
    nomes = input("Digite o nome:")
    idades = str(input("Digite idade: "))
    curso = input("Digite Curso: ")
    lista_geral= [nomes, idades, curso]
    lista_completa.append(lista_geral)
    i += 1
print(lista_completa)

# Ex. 15 - Crie um programa que solicite números para o usuário, pare quando digitar 0, armazene em uma lista. Mostre a lista completa e a soma dos valores.
listaNumeros = []
somas = 0

while True:
    numeros = int(input("Digite um número: "))
    if numeros == 0:
        break
    listaNumeros.append(numeros)
    somas += numeros
print(somas)

