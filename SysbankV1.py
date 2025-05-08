# Passo 1: Criar variáveis para representar o saldo e a opção do menu

saldo = 0.0
opcao = 0 ##

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

# Aqui você pode adicionar a lógica para cada opção do menu

if opcao == 1:

    print(f"Seu saldo atual é: R$ {saldo:.2f}")

elif opcao == 2:

    valor_deposito = float(input("Digite o valor a depositar: "))
    saldo += valor_deposito
    print(f"Depósito de R$ {valor_deposito:.2f} realizado com sucesso.")
    print(f"Seu novo saldo é: R$ {saldo:.2f}")

elif opcao == 3:

    valor_saque = float(input("Digite o valor a sacar: "))
    if valor_saque < saldo:
        saldo -= valor_saque
        print(f"Saque de R$ {valor_saque:.2f} realizado com sucesso.")
        print(f"Seu novo saldo é: R$ {saldo:.2f}")

    else:

        print("Saldo insuficiente.")

elif opcao == 4:

    print("Obrigado por utilizar nosso banco virtual!")

    '''Erros cometidos:
    1 - Eu esqueci de adicionar a linha opcao_str = input("Digite a opção desejada) e ao rodar com uma letra pra testar
    a validação do erro, ficou em um loop infinito já que não tinha uma forma de parar o loop while sem o input.
    
    2 - Eu confundi a linha opcao = int(opcao_str) pra ficar como opcao_str = int(opcao_str) e ao colocar qualquer número
    o código não rodava os ifs e finalizava o programa.
    
    Uma possível melhoria seria deixar as opções rodando até que o cliete escolha sair do programa, para que ele possa
     realizar múltiplas operações sem precisar reiniciar o programa.
     
     '''