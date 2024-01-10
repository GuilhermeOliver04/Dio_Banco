limite = 500
saldo = 0
extrato = ''
saques = 0
Limite_Saque = 3
while 1 == 1:
    opcao = int(input('[1] Sacar: \n[2] Deposito: \n[3] Extrato: \n[0] Sair: \n==>:'))

    if opcao == 2:
        valor = float(input('Qual o valor do Deposito: '))
        if valor > 0:
            saldo += valor
            extrato += f'Deposito: R${valor:.2f}\n'

        else:
            print('Opção invalida, refaça a operação.') #ultima linha do codigo de deposito

    elif opcao == 1:
        valor = float(input('Informe o valor do saque: '))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saque = saques >= Limite_Saque

        if excedeu_saldo:
            print('Valor não disponivel.')

        elif excedeu_limite:
            print('Limite maximo por saque ultrapassado.')

        elif excedeu_saque:
            print('Limite de saque diario atingido.')

        elif valor > 0:
            saldo -= valor
            extrato += f'Saque: R${valor:.2f}\n'
            saques += 1

        else:
            print('Operação invalida, valor invalido')

    elif opcao == 3:
        print('*'*30)
        print('Informações não encontradas.' if not extrato else extrato)
        print(f'\n Saldo: R${saldo:.2f}')

    elif opcao == 0:
        break


print('Opcão invalida porfavor refaça a operação.')