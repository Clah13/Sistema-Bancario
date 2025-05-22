saldo = 1000.00 #Saldo Inicial

def consultar_saldo():
    """Exibe o saldo atual"""
    print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print(f"Seu saldo atual é: R${saldo:.2f}")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

def sacar():
    """Realiza a operação de saque, verificando o saldo."""
    global saldo # Indica que estamos modificando a variável global saldo

    while True:
        try:
            valor_saque = float(input("Digite o valor a sacar: R$ "))
            break # Sai do loop se a entrada for válida
        except ValueError:
            print("Valor inválido. Por favor, digite um número.")

    if valor_saque <= saldo:
        saldo -= valor_saque
        """Obs: quando se digita um número com vírgula, ele arredonda o valor a ser subtraído para cima (1055.67 - 999.99 = 55.67 (55.68))."""
        #Sugestão : usar módulo decimal (from decimal import Decimal)
        print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print(f"Saque de R${valor_saque:.2f} realizado com sucesso.")
        print(f"Seu novo saldo é: R${saldo:.2f}")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    else:
        print("Saldo Insuficiente.")

def depositar():
    """Realiza a operação de depósito."""
    """Obs: quando se digita um número com múltiplas casas decimais, ele arredonda o valor para cima."""
    global saldo # Indica que estamos modificando a variável global saldo

    while True:
        try:
            valor_deposito = float(input("Digite o valor a depositar: R$ "))
            break # Sai do loop se a entrada for válida
        except ValueError:
            print("Valor inválido. Por favor, digite um número.")

    saldo += valor_deposito
    print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print(f"Depósito de R${valor_deposito:.2f} realizado com sucesso.")
    print(f"Seu novo saldo é: R${saldo:.2f}")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

# ... código principal com o loop while

while True:

    #Exibir mensagem de boas-vindas e as opções do menu
    print("\nOlá! Bem-vindo ao seu banco virtual.")
    print("--------------------------------------")
    print("1 - Consultar saldo")
    print("2 - Depositar")
    print("3 - Sacar")
    print("4 - Sair")
    print("--------------------------------------")

    #Ler a opção do usuário
    while True:
        try:
            opcao_str = input("Digite a opção desejada: ")
            opcao = int(opcao_str)
            if 1<= opcao <= 4:
                break # Sai do loop se a opção for válida
            else:
                print("Opção inválida. Por favor, digite um número entre 1 e 4.")
        except ValueError:
            print("Opção inválida. Por favor, digite um número inteiro.")

    # Executar a ação com base na opçao do usuário

    if opcao == 1:
        consultar_saldo()
    elif opcao == 2:
        depositar()
    elif opcao == 3:
        sacar()
    elif opcao == 4:
        print("Obrigado por utilizar nosso banco virtual!")
        break # Sai do laço while, encerrando o programa.

