pessoas = int(input('Quantidade de pessoas no quarto: '))
quarto = []
for pessoa in range(pessoas):
    nome = input('Nome completo: ')
    cpf = input('CPF: ')
    while len(cpf) != 11:
        print('CPF inválido, digite novamente.')
        cpf = input('CPF: ')
    else:
        hospede = [f'{nome}, cpf:{cpf}']
        quarto.append(hospede)
print(quarto)