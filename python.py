#cliente = listaFila.pop(0) -- .pop é para EXCLUIR o valor escolhido dentro da lista -- valor = posição da lista
#print(listaFila)
listaFila = ['cliente1','cliente2','cliente3']

while listaFila:
    cliente = listaFila.pop(0)
    print(f"Atendendo {cliente}")

# 1 - Sistema de login com nível de acesso. Solitece usuário e senha. Se usuário é igual a admin, crie uma estrutura de condição aninhada para colicitar senha e se a mesma for "1234", mostre que o usuário terá acesso total. Caso o usuário insira senha incorreta, mostre "senha incorreta". Caso usuário insira nome incorreto, exiba "nome incorreto".

usuario = input("Digite seu nome")

if usuario == "admin":
    senha = input("Digite sua senha:")
        
    if senha == "1234":
        print("acesso total liberado")
    else:
        print("Senha incorreta!")

else:
    print("Usuário inválido!")

# 2 - 

idade = int(input("Digite sua idade"))

if idade >= 60:
    print("Idoso")
elif idade >= 18:
    print("Adulto")
elif idade >= 12:
    print("Adolescente")
else:
    print("Criança")

# 3 -

nota = int(input("digite sua note: "))

if nota >= 6:
    print("Aprovado")
    
    if nota >= 9:
        print("Aprovado com excelência!")
else:
    print("reprovado!")

# 4 -

numero = int(input("Digite um número: "))

if numero >= 0:
    print("Positivo")
    if numero % 2 == 0:
        print("e par")
    else:
        print("e ímpar")
else:
    print("Negativo")
    if numero % 2 == 0:
        print("e par")
    else:
        print("e ímpar")

# 5 -

valor = int(input("digite valor: "))

if valor >= 200:
    nomeVip = input("digite seu nome")
    if nomeVip == "Guilherme":
        print("Desconto VIP de 20%")
    else:
        print("Desconto de 10%")
else:
    print("Sem desconto!")

# 6 -

diaSemana = input("Digite o dia da semana: ")

if diaSemana == "sabado":
    print("dia de festa")
elif diaSemana == "domingo":
    saude = input("qual sua condição fisica?")
    if saude == "dores de cabeça":
        print("recuperando")
    else:
        print("saudavel")
else:
    print("Trabalhando trabalhando e trabalhando...")

