# Ex. 1 - Lista de números

numeros = []

for i in range(5):
    numero = int(input("Digite um número: "))
    numeros.append(numero)
    print(numeros)

# Ex. 2 - Lista de números e nomes

numeros2 = []
nomes = []

for i in range(5):
    numero = int(input("Digite um número: "))
    nome = input("Digite um nome: ")


    numeros2.append(numero)
    nomes.append(nome)
    print(numeros2)
    print(nomes)

# Ex. 3 - listas de números e nomes

listaUniversidade = ['USP', 'FIAP', 'UNICAMP', 'UNESP', 'MIT']
r = 1
for k in listaUniversidade:
    if k == 'MIT':
        break

    print(f"{r}° Universidade - {k}")
    r += 1

# Ex. 4 - Estrutura com  continue

listaUniversidade = ['USP', 'FIAP', 'UNICAMP', 'UNESP', 'MIT']
n = 1
for h in listaUniversidade:
    if h == 'UNESP':
        continue

    print(f"{n}° Universidade - {h}")
    n += 1,

# Ex. 5 - Soma e Média de valores digitados pelo usuário. Crie um algoritmo para solicitar 5 valores não inteiros, insira em uma lista. Após isso, crie uma estrutura para somar e retornar a média dos elementos desta lista.

listaNumNaoInteriros = []

for t in range(5):
    numerosEscolhidos = float(input("Digite um número NÃO inteiro: "))
    listaNumNaoInteriros.append(numerosEscolhidos)

media = sum(listaNumNaoInteriros)/len(listaNumNaoInteriros)
print(f"A média é {media}")

# Ex. 6 - Crie uma estrutura para solicitar 10 números para o usuário. Após isso crie duas listas (par e impar) e insira os valores par na lista par, valores ímpares na lista ímpar. Print a lista completa, lista par e lista ímpar.

num = [] #Lista dos números escolhidos - só será usado para listar os números escolhidos e não para o funcionamento do algoritmo.
par = [] #Lista dos números pares
impar = [] #Lista dos números ímpares

for j in range(10): #range(10) - para solicitar 10 números ao usuário
    numEscolhido = int(input("Digite um número: "))
    if numEscolhido % 2==0:
        par.append(numEscolhido)
    if numEscolhido % 2!=0:
        impar.append(numEscolhido)
num.append(numEscolhido)
print(f"Os números escolhidos foram {num}")
print(f"os pares são: {par}")
print(f"os ímpares são: {impar}")

# Ex. 7 - Crie um algoritmo para cadastro de alunos, onde deve ser solicitado nome e idade 5 vezes, porém, a informação deve aparecer com lista dentro de lista, ou seja, [nome1 , idade1], [nome2 , idade2], [nome3 , idade3], [nome4 , idade4], [nome5 , idade5]. Print a lista final.

listaUsuario = []
listaGeral = []

for l in range(5):
    nomesAlunos = str(input("Digite seu nome: "))
    idadeAlunos = int(input("Digite sua idade: "))
    
    listaUsuario = [nomesAlunos, idadeAlunos]
    listaGeral.append(listaUsuario)
print(listaGeral)

# Ex. 8 - Vamos fazer um algoritmo para cadastro com média. Solicite 3 informações: nome, nota1 e nota2 três vezes. Após isso, calcule a média de cada aluno e retorne uma lista contendo nome, nota1, nota2 e média de cada aluno. 

listaUnica = []

for l in range(3):
    nome3 = str(input("Digite seu nome: "))
    nota1 = float(input("Digite sua nota: "))
    nota2 = float(input("Digite sua segunda nota:"))

    mediaNota = (nota1 + nota2)/2
    listaAlunoNota = [nome3, nota1, nota2, mediaNota]
    listaUnica.append(listaAlunoNota)

print(listaUnica)

# Ex. 9 - Crie um algoritmo para simular um sistema de compras, onde deverá ser solicitado nome 100x. Após isso, crie uma estrutura para quebrar a solicitação de nomes. Após isso, crie uma estrutura para solicitar preço, com isso, deixe o respectivo nome e preço juntos. Finalmente, mostre o valor total dos produtos.

list = []
valorTotal = 0


for i in range(100):
    name = str(input("Digite o nome: ").lower())
    
    if name == "exit":
        break

    preco = float(input("Digite o valor do preço: "))
    valorTotal += preco

    listaNomePreco = [name, preco]
    list.append(listaNomePreco)

print(list)
print("Valor total: ", valorTotal)

# Ex. 10 - Crie um algoritmo para solicitar o nome e nota para 4 alunos. Insira em uma estrutura com lista dentro de lista (nome, nota). Após isso, crie uma estrutura para mostrar os alunos aprovados com nota maior ou igual 6, mostrando o respctivo nome e nota. Crie também uma estrutura para mostrar os alunos com nota menor que 6, mostrando o respctivo nome e nota.

listaAprovados =[]
listaReprovados = []
notaAprovados = []
notaReprovados = []

for p in range(4):
    nomeAluno2 = str(input("Digite seu nome: "))
    notaInt = float(input("Digite sua nota: "))

    if notaInt >= 6:
        listaAprovados.append(nomeAluno2)
        listaAprovados.append(notaInt)
    elif notaInt < 6:
        listaReprovados.append(nomeAluno2)
        listaReprovados.append(notaInt)

print(f"os alunos aprovados foram: {listaAprovados}")
print(f"os alunos reprovados foram: {listaReprovados}")


#Outra solução do Ex. 10 

l = []

for i in range(4):
    n = str(input("Digite seu nome: "))
    nt = float(input("Digite sua nota: "))
    la = [n, nt]
    l.append(la)

print(l)

for a in l:
     if a[1] >= 6:
        print(f"Aluno: {a[0]} Aprovado")
     elif a[1] < 6:
        print(f"Aluno: {a[0]} Reprovado")

# Ex. 11 - Crie um algoritmo para simular sistema com menu. o Usuário pode cadastrar, listar ou sair da estrutura. Se opção l, solicite nome, idadem cidade e deixe esar informações em uma estrutura de lista dentro de lista. Se opção 2, print o respectivo nome, idade e cidade da pessoa. Se opção 3, crie uma estrutura para sair do código.

list2 = []

while True:
    opcao = str(input("Digite a sua opção 1- cadastro, 2- mostrar, 3- sair").lower())
    if opcao == "cadastro" or opcao == "1":
        listUser = []
        name2 = str(input("Digite o nome: "))
        age = int(input("Digite a idade: "))
        cidade = str(input("Digite a sua cidade: "))
        listUser.append(name2)
        listUser.append(age)
        listUser.append(cidade)
        list2.append(listUser)
    elif opcao == "mostrar" or opcao == "2":
        print(list2)
    elif opcao == "sair" or opcao == "3":
        print("Até mais")
        break
    else:
        print("Digite uma opção válida!")


# Ex. 12 -  Criando uma Matriz (3X3) usando estrutura de repetição

list3 = [[],[],[]]
coluna = 0

for x in range(3):
    coluna += 1
    li2 = 1
    for z in range(3):
        valor = int(input(f"Digite um valor da coluna {coluna} da linha {li2}: "))
        list3[x].append(valor)
        li2 += 1
        
print(list3)
