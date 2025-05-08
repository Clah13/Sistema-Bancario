# Passo 1: Criar variáveis para representar o saldo e a opção do menu.

saldo = 1000.0 # Saldo inicial (você pode alterar este valor)
opcao = 0

#Etapa 2 passo 1

def consultar_saldo():
    """Exibe o saldo atual."""
    print(f"Seu saldo atual é: R$ {saldo:.2f}")

def sacar():
    """Realiza a operação de saque, verificando o saldo."""
    global saldo # Indica que estamos modificando a variável global saldo
    valor_saque = float(input("Digite o valor a sacar: "))
    if valor_saque <= saldo:
        saldo -= valor_saque
        print(f"Saque de R$ {valor_saque:.2f} realizado com sucesso.")
    else:
        print("Saldo insuficiente.")

def depositar():
    """Realiza a operação de depósito."""
    global saldo #Indica que estamos modificando a variável global saldo
    valor_deposito = float(input("Digite o valor a depositar: R$ "))
    saldo += valor_deposito
    print(f"Depósito de R${valor_deposito:.2f} realizado com sucesso.")

# Passo 2: Exibir uma mensagem de boas-vindas e as opções do menu

print("Olá! Bem-vindo ao seu banco virtual.")
print("--------------------------------------")
print("1 - Consultar Saldo")
print("2 - Depositar")
print("3 - Sacar")
print("4 - Sair")
print("--------------------------------------")

# Passo 3: Ler a opção do usuário

opcao_str = input("Digite a opção desejada: ")

# Passo 4: Validar a opção do usuário usando um laço while

while not opcao_str.isdigit() or not (1 <= int(opcao_str) <= 4):
    print("Opção inválida. Por favor, digite um número entre 1 e 4.")
    opcao_str = input("Digite a opção desejada: ")

opcao = int(opcao_str)

# Executar a ação com base na opção do usuário

if opcao == 1:

    consultar_saldo()

elif opcao == 2:

    depositar()

elif opcao == 3:

    sacar()

elif opcao == 4:

    print("Obrigado por utilizar nosso banco virtual!")