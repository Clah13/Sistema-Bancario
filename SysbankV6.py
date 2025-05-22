import datetime

saldo = 1000.0 #saldo inicial
extrato = [] # Lista para armazenar as transações

def consultar_saldo():
    """Exibe o saldo atual"""
    print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print(f"Seu saldo atual é: R${saldo:.2f}")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

def sacar():
    """Realiza a operação de saque, verificando o saldo."""
    global saldo, extrato

    while True:
        try:
            valor_saque = float(input("Digite o valor a sacar: R$ "))
            break
        except ValueError:
            print("Valor inválido. Por favor, digite um número.")

        if valor_saque <= saldo:
            saldo -= valor_saque
            agora = datetime.datetime.now()
            extrato.append({"data_hora": agora, "tipo": "Saque", "valor": valor_saque})

            print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            print(f"Saque de R${valor_saque:.2f} realizado com sucesso.")
            print(f"Seu novo saldo é: R${saldo:.2f}")
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        else:
            print("Saldo insuficiente.")

def depositar():
    """Realiza a operação de depósito."""
    global saldo, extrato

    while True:
        try:
            valor_deposito = float(input("Digite o valor a depositar: R$ "))
            break
        except ValueError:
            print("Valor inválido. Por favor, digite um número.")
    saldo += valor_deposito
    agora = datetime.datetime.now()
    extrato.append({"data_hora": agora, "tipo": "Depósito", "valor": valor_deposito})

    print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print(f"Depósito de R${valor_deposito:.2f} realizado com sucesso.")
    print(f"Seu novo saldo é: R${saldo:.2f}")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

def exibir_extrato():
    """Exibe o extrato bancário."""
    global extrato
    if not extrato:
        print("Não foram realizadas transações.")
    else:
        print("\n--- Extrato Bancário ---")
        for transacao in extrato:
            data_hora = transacao["data_hora"].strftime("%d/%m/%Y %H:%M:%S")
            tipo = transacao["tipo"]
            valor = transacao["valor"]
            print(f"{data_hora} - {tipo}: R$ {valor:.2f}")
        print(f"Saldo atual: R${saldo:.2f}")

# ... código principal com o loop while

while True:

    #Exibir mensagem de boas-vindas e as opções do menu
    print("\nOlá! Bem-vindo ao seu banco virtual.")
    print("--------------------------------------")
    print("1 - Consultar saldo")
    print("2 - Depositar")
    print("3 - Sacar")
    print("4 - Exibir extrato")
    print("5 - Sair")
    print("--------------------------------------")

    #Ler a opção do usuário
    while True:
        try:
            opcao_str = input("Digite a opção desejada: ")
            opcao = int(opcao_str)
            if 1<= opcao <= 5:
                break # Sai do loop se a opção for válida
            else:
                print("Opção inválida. Por favor, digite um número entre 1 e 5.")
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
        exibir_extrato()
    elif opcao == 5:
        print("Obrigado por utilizar nosso banco virtual!")
        break # Sai do laço while, encerrando o programa.


