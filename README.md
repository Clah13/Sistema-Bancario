# Roteiro de Práticas 04 e 05 - Sistema Bancário

O roteiro tem como objetivo principal criar um programa que simule as operações realizadas em um sistema bancário.
Suas atividades são incrementais, em que o primeiro código representa um MVP e os códigos subsequentes representam atualizações das entregas anteriores.

> [!important]
> **Para este programa, o repositório armazenará arquivos de dois roteiros diferentes, mas que representam a continuação do mesmo programa. Os roteiros foram separados em duas seções (de semanas diferentes) para facilitar a entrega do aluno.**

Os códigos seguem um roteiro fixo criado pelo professor.

**Nenhuma IA foi utilizada neste desenvolvimento.**
## Etapas de desenvolvimento

### Roteiro 04

Etapa 1: Apresentação e Menu [*SysbankV1.py*]

  > Implementa um menu e suas respectivas operações básicas: Consulta de Saldo, Depósito, Saque e Saída do Programa. Valida as opções do usuário.

Etapa 2: Implementação das Operações [*SysbankV2.py*]

  > Refatora o código anterior para agrupar as principais operações em funções específicas.

Etapa 3: Laço Principal [*SysbankV3.py*]

  > Implementa um laço while no menu de opções, para que o usuário faça todas as operações desejadas até optar em sair.
### Roteiro 05

Etapa 4: Validação de Entrada Robusta [*SysbankV4.py*]

> Valida erros na entrada de dados em todas as operações relevantes, incluindo saque e o menu. Conta com orientações específicas para o erro encontrado.

Etapa 5: Extrato Bancário Detalhado [*SysbankV5.py*]

> Introdução da variável global extrato, da função que consulta o extrato. Refatoração das demais funções para registrar no extrato e adaptação do menu para acomodar o novo item.

Etapa 6: Persistência de Dados (Básico) [*SysbankV6.py*]

> Implementa um método de registro histórico das movimentações em um arquivo .txt via formato JSON que poderá ser consultado a qualquer momento quando o usuário pedir o extrato.

Etapa 7: Desafio [*SysbankDesafio.py*]

> Implementa a função que faz transferências bancárias, ajusta o menu para acessar a nova opção e adiciona o evento no extrato.
