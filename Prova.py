#lista para armazenamento de dados
armazenamento = []

#laço de repetição
while True:
    # Na variavel mes, somente irá entrar números de 1 até 12. TENHO QUE FAZER O TRATAMENTO COM ESTÁ EXIGENCIA!
    mes = str(input('Informe o mês: '))


    # Entrada do salario.
    salario = float(input('Informe seu salário no mês: '))

    # Calculando valor que será investido, ou seja, os 10% do salário.
    porcento_10 = ((salario * 10)/100)

    # calculando o juros sobre o investimento, ou seja, o 1% sobre os 10% retirados do salário.
    porcento_1 = (porcento_10 * 1)/100

    # calculando despesas
    despesa_mensal = (salario-porcento_10)


    armazenamento.append(['salário:',salario,'mês:',mes,'despesa do mês:',despesa_mensal])

    print(armazenamento[0][1])

    # Questionando se vai prescisar alterar o salário que foi adicionado na variavel acima (salario).
    alterador = input('Quer alterar? S/N').upper() != "S"


    if alterador == "S":
        # Entrando o novo salario alterado.
        novo_salario = input('Informe seu rendimento no mês: ')
        # na variavel armazenamento bloco 0 na posição 1.
        armazenamento[0][1]= novo_salario




    if input("Deseja continuar? (S/N)").upper() != "S":
            break

print('\n\n\n')
print(armazenamento)
print(f'Este é o salario adicionado :{salario}')
print(f'Este é o valor que vai ser investido neste mês : {porcento_10}')
print(f'Este é o valor recebido do investimento no juros de 1% :{porcento_1}')
print(f'A despesa mensal foi de {despesa_mensal}')