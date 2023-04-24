
dados = []

while True:

    n = open('Arquivo.txt', 'w')
    try:
        # Iniciando variavel mês, PRESCISO FAZER O TRATAMENTO DE EXCESSOES AQUI!
        mes = int(input('Informe o seu mês:'))
        salario = float(input('Informe seu salário:'))

        alterar_salario = str(input('Quer alterar? [S/N]')).upper().split()[0]
    except(ValueError, TypeError):
        print('Valor incorreto')
    else:

        if alterar_salario == 'S':
            novo_salario = float(input('Informe o novo salario:'))
            salario = novo_salario

        # Calculando valor que será investido, ou seja, os 10% do salário.
        porcento_10 = ((salario * 10)/100)

        # calculando o juros sobre o investimento, ou seja, o 1% sobre os 10% retirados do salário.
        porcento_1 = (porcento_10 * 1) / 100
        # calculando despesas
        despesa_mensal = (salario - porcento_10)

        n.write(f"{mes},{salario},{porcento_10},{porcento_1},{despesa_mensal}\n")

        pergunta = str(input('Quer continuar? [S/N]:')).upper().split()[0]

        if pergunta == 'N':
            break
        if pergunta != 'N' and pergunta != 'S':
            break


print('\n\n\n')
