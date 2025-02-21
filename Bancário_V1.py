# Menu inicial
menu = '''
Bem vindo! Qual operação você deseja fazer?

===========================================

[1] - Depósito
[2] - Sacar
[3] - Extrato Bancário
[4] - Finalizar Atendimento

===========================================

=> '''

# Declaração de valores
valor = 0
valor_conta = 0
limite_saque = 0
limite_diário = 0
extrato = ""
nova_operacao = True

# Função para verificação de atendimento novamente
def Verificacao():
    valor_verificacao = int(input('''Deseja fazer mais uma operação? \n 1 - Sim / 2 - Não \n => '''))
    if valor_verificacao == 1:
        return True
    else:
        return False

# Função de verificação de valor decimais
def Verificacao_decimal():
    global valor
    verifica = valor.split(".")
    if len(verifica[1]) > 2:
        return False
    else:
        return True

# Verificação para realizar o serviço novamente
def realizar_servico_novamente():
    print("Valor inválido!")
    nova_operacao = Verificacao()

# Processamento de dados
while nova_operacao:
    # verificação de serviço
    operacao = True

    # entrada de valores
    opcao = int(input(menu))
    # conferindo as questões
    if opcao == 1:
        valor = float(input("Digite o valor desejado de depósito:\n => "))
        # Verificação de valor positivo
        if valor > 0:
            if Verificacao_decimal:
                valor_conta += valor
                extrato += f'Depósito: + R${valor:.2f}\n'
                print(f'Valor Depósitado: {valor}')
                # chama a função de verificação de atendimento
                realizar_servico_novamente()
            else:
                operacao = False
                realizar_servico_novamente()
        else:
            realizar_servico_novamente()
    elif opcao == 2:
        valor = float(input("Digite o valor desejado para sacar:\n => "))
        if valor_saque > 0:
            if valor_conta > valor:
                valor_conta -= valor
                extrato += f'Saque: -R${valor:.2f}\n'
                print(f'Valor Sacado: R${valor}')
                # chama a função de verificação de atendimento
                realizar_servico_novamente()
            else:
                print("Saldo Insuficiente! Valor disponível: R${valor:.2f}")
                realizar_servico_novamente()