# importação de data/tempo do programa
import datetime

# Menu inicial
menu = '''
Bem-vindo! Qual operação você deseja fazer?

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
data_atual = datetime.date.today()
saques_realizados = 0
extrato = ""
nova_operacao = True


# Função de verificação de valor decimais
def Verificacao_decimal(number):
    verifica = str(number).split(".")  

    if len(verifica) == 1:  
        return True

    if len(verifica[1]) > 2:  
        return False
    else:
        return True

# Verificação para realizar o serviço novamente
def realizar_servico_novamente():
    while True:
        try:
            confirma = int(input("Deseja realizar mais uma operação?\n 1 - Sim / 2 - Não\n => "))
            if confirma not in [1, 2]:  # Corrigido!
                raise ValueError("Número inválido")
            return confirma == 1  # Retorna True se 1, False se 2
        except ValueError as e:
            print(f'Erro! {e}. Tente novamente.')

# Função para erro
def Verificacao():
    global opcao
    if opcao != 3:
        print("Erro! Valor Inválido. Tente novamente")
    return realizar_servico_novamente()

# Função para liberar 3 saques diario
def pode_sacar():
    global data_atual, saques_realizados

    # resetar data do horário
    if datetime.date.today() != data_atual:
        data_atual = datetime.time.today()
        saques_realizados = 0
    # verificação de saques realizados
    return saques_realizados < 3
    
# Função para encerrar o atendimento
def encerrar_atendimento():
    print("Obrigado pela preferência! Até mais 😊")
    

# Processamento de dados
while True:
    try:
        opcao = int(input(menu))  # Evita erro de input inválido
    except ValueError:
        print("Erro! Digite um número válido.")
        continue  # Volta ao menu inicial

    if opcao == 1:
        try:
            valor = float(input("Digite o valor desejado de depósito:\n => "))
            if valor > 0:
                if Verificacao_decimal(valor):
                    valor_conta += valor
                    extrato += f'Depósito: + R${valor:.2f}\n'
                    print(f'Valor Depositado: R${valor:.2f}')
                    if not realizar_servico_novamente():
                        encerrar_atendimento()
                        break
                else:
                    if not Verificacao():
                        encerrar_atendimento()
                        break
            else:
                if not Verificacao():
                    encerrar_atendimento()
                    break
        except ValueError:
            if not Verificacao():
                encerrar_atendimento()
                break

    elif opcao == 2:
        if pode_sacar():
            try:
                valor = float(input("Digite o valor que deseja sacar: "))
                if valor > 0:
                    if Verificacao_decimal(valor):
                        if valor_conta > valor:
                            valor_conta -= valor
                            saques_realizados += 1
                            extrato += f'Saque:    - R${valor:.2f}\n'
                            print(f'Valor Sacado: R${valor:.2f}')
                            if not realizar_servico_novamente():
                                encerrar_atendimento()
                                break
                        else:
                            print(f"Valor não disponível em sua conta. Saldo: {valor_conta}")
                            if not realizar_servico_novamente():
                                encerrar_atendimento()
                                break
                    else:
                        if not Verificacao():
                            encerrar_atendimento()
                            break
            except ValueError:
                if not Verificacao():
                    encerrar_atendimento()
                    break
        else:
            print("O limite diário de saque já foi atingido. Tente novamente mais tarde.")
            if not realizar_servico_novamente():
                encerrar_atendimento()
                break
    elif opcao == 3:
        print("\n==================EXTRATO==================\n")
        print(extrato if extrato else "Nenhuma movimentação realizada")
        print(f'Saldo: R${valor_conta}')
        print("\n===========================================\n")
        if not Verificacao():
            encerrar_atendimento()
            break
    elif opcao == 4:
        encerrar_atendimento()
        break