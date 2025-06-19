saldo = 1000.00  # Saldo inicial (o valor pode ser alterado)

def consultar_saldo():
    """Exibe o saldo atual"""
    print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print(f"Seu saldo atual é: R${saldo:.2f}")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

def sacar():
    """Realiza a operação de saque, verificando o saldo."""

    global saldo  # Indica que estamos modificando a variável global saldo
    while True:
        try:
            valor_saque = float(input("Digite o valor a sacar: R$ "))
            break  # Sai do loop se a entrada for válida.
        except ValueError:
            print("Valor inválido. Por favor, digite um número.")

    if valor_saque <= saldo:
        saldo -= valor_saque
        print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print(f"Saque de R${valor_saque:.2f} realizado com sucesso.")
        print(f"Seu novo saldo é: R$ {saldo:.2f}")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    else:
        print("Saldo Insuficiente.")


def depositar():
    """Realiza a operação de depósito."""
    global saldo  # Indica que estamos modificando a variável global saldo
    while True:
        try:
            valor_deposito = float(input("Digite o valor a depositar: R$ "))
            break  # Sai do loop se a entrada for válida
        except ValueError:
            print("Valor inválido. Por favor, digite um número.")
    saldo += valor_deposito

    print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print(f"Depósito de R${valor_deposito:.2f} realizado com sucesso.")
    print(f"Seu novo saldo é: R$ {saldo:.2f}")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")


# Código principal com um laço while

while True:

    # Exibir mensagem de boas-vindas e as opções do menu
    print("\nOlá! Bem-vindo ao seu banco virtual.")
    print("--------------------------------------")
    print("1 - Consultar saldo")
    print("2 - Depositar")
    print("3 - Sacar")
    print("4 - Sair")
    print("--------------------------------------")

    # Validar a opção do usuário usando um laço While

    while True:
        try:
            opcao_str = input("Digite a opção desejada: ")
            opcao = int(opcao_str)

            if 1 <= opcao <= 4:
                break  # Sal do loop se a opção for válida

            else:
                print("Opção Inválida. Por favor, digite um número entre 1 e 4.")
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
        break  # Sai do laço while, encerrando o programa.
