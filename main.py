menu = """ 
_____________________________________________
    Bem vindo(a) ao banco do estudante

    SELECIONE A OPÇÃO DESEJADA : 
    
    DEPOSITO - PRESSIONE 'D'
    SAQUE - PRESSIONE 'S'
    EXTRATO - PRESSIONE 'E'
    SAIR - PRESSIONE 'Q'
______________________________________________    
"""
saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    print(menu)
    opcao = input()

    if opcao == "d":
        print(f"Digite o valor que deseja depositar:\n")
        saldo += int(input())
    
    elif opcao == "s":
        if numero_saques >= 3:
            print(f"Não será possível realizar o saque pois voce ultrapassou o limite de 3 saques por dia\n")
        print(f"Digite o valor que deseja sacar:\n")
        saque = int(input())
        numero_saques += 1
        if limite <= 0:
            print(f"Não será possível realizar saques pois voce ultrapassou o limite diário de 500 reais\n")
            numero_saques -= 1
            print(f"\nPressione qualquer tecla para sair!")
            continuar = input()
        elif saque > saldo:
            print(f"O valor que voce está tentando sacar é maior que seu valor em conta\n")
            numero_saques -= 1
            print(f"\nPressione qualquer tecla para sair!")
            continuar = input()
        elif limite >= saque and saque <= saldo:
            print(f"Operação realizada com sucesso!")
            saldo -= saque
            limite -= saque
            print(f"\nPressione qualquer tecla para sair!")
            continuar = input()

    elif opcao == "e":
        print(f"Seu saldo é de R${saldo} \nO seu limite diario para saques é R${limite} \nVoce ja utilizou {numero_saques} saques dos 3 saques que tem por dia!")
        print(f"\nPressione qualquer tecla para sair!")
        continuar = input()
    
    elif opcao == "q":
        print( "-" * 30)
        print(f"Encerrando a operação!")
        print( "-" * 30)
        break
    
    else:
        print(f"Opção inválida, por favor selecione outra!")
        print(f"\nPressione qualquer tecla para sair!")
        continuar = input()



        