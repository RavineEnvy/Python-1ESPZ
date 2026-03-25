#Site bom para testar código - pythontutors

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

# 2 - Classificação de idade. Solicite idade, se idade for maior ou igual a 10, crie uma estrutura de condição aninhada para verificar se a idade é maior ou igual a 60, se for, mostre o resultado "idoso", caso seja maior ou igual a 18, mostre o resultado "adulto", maior ou igual a 12, mostre o resultado "criança".

idade = int(input("Digite sua idade"))

if idade >= 18:
    if idade >= 60:
        print("Idoso!")
    else:
        print("Adulto!")
else:
    if idade >= 12:
        print("Adolescente!")
    else:
        print("Criança!")

# 3 - Aprovação com distinção, solicite nota, se nota for maior ou igual a 6, crie condição aninhada para verificar se a nota é maior ou igual a 9, se for, "aprovado com excelência". Se nota não for maior ou igual a , "Aprovado". Caso contrário, "Reprovado".

nota = int(input("digite sua nota: "))

if nota >= 6:
    print("Aprovado")
    
    if nota >= 9:
        print("Aprovado com excelência!")
else:
    print("reprovado!")

# 4 - Verificação de número. Solicite número e verifique se é maior ou menor que zero, se for, crie uma estrutura de condição aninhada para verificar se este número é par ou ímpar. 

numero = int(input("Digite um número: "))

if numero != 0:
    if numero > 0:
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
else:
    print("O número é 0(Par)")

# 5 - Sistema de desconto. solicite valor e se a pessoa é vip ou nãp. Se valor for maior ou igual a 200, crie uma estrutura de condição aninhada para verificar se a pessoa é vip, se for, ofereça 20% de desconto e mostre o valor final (após desconto) Se não for vip, ofereça 10% de desconto.

valor = int(input("digite valor: "))

if valor >= 200:
    nomeVip = input("digite seu nome")
    if nomeVip == "Guilherme":
        desconto = valor * (20/100)
        valorPagar = valor - desconto
        print(f"Desconto VIP de 20%, Total a pagar de: R${valorPagar},00")
    else:
        desconto = valor * (10/100)
        valorPagar = valor - desconto
        print(f"Desconto de 10%, Total a pagar de: R${valorPagar},00")
else:
    print("Sem desconto!")

# 6 - Crie um algoritmo para perguntar qual o dia da semana, caso seja sábado, escreva dia de festa. Caso seja, domingo pergunte sobre a condição física do usuário, se estiver com dores de cabeça, mostre "recuperando, então precisa descansar." Casó contrário mostre "Trabalhando, trabalhando e trabalhando...."

diaSemana = input("Digite o dia da semana: ")

if diaSemana == "sabado":
    print("dia de festa")
elif diaSemana == "domingo":
    saude = input("qual sua condição fisica?")
    if saude == "bom":
        print("Está apenas descansando!")
    else:
        print("Ressaca!")
else:
    print("Trabalhando, trabalhando e trabalhando...")

# 7 - Crie um algoritmo para soliciar a escolha do menu do café da manhã. 
# 1. Ovos.
# 2. Panquecas.
# 3. Wafles.
# 4. Frutas.
# se for ovos, pergunte qual o tipo de acompanhamento. Caso for frutas, pergunte qual o tipo de fruta e acompanhamento. Para caso, traga uma informação com print para o usuário.

cafeManha = input("Qual será seu café da manhã?: ")

if cafeManha == "Ovos":
    acompanhamento = input("Qual acompanhamento?")
    if acompanhamento == "Pão":
        print("Você escolheu um delicioso pão com ovo!")
    else:
        print(f"Você escolheu {cafeManha} com {acompanhamento}.")
elif cafeManha == "Panquecas":
    mel = input("Deseja mel?")
    if mel == "sim":
        print("Panquecas com mel.")
    else:
        print("Apenas panquecas.")
elif cafeManha == "Wafles":
    manteiga = input("Deseja manteiga?")
    if manteiga == "sim":
        print("Wafle amanteigado!")
    else:
        print("Apenas Wafle.")
elif cafeManha == "frutas":
    citricas = input("deseja frutas citricas?")
    if citricas == "sim":
        print("você esolheu laranja")
    else:
        print("você escolheu maça")
