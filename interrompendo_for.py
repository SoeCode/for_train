#Melhor eficiência e desempenho do código:

#Primeiro exemplo usando BREAK:
    #caso a loja não atinja a meta de vendas:
    #Break na primera venda abaixo da média.
vendas = [27, 56, 29, 89, 4,
          67, 45, 6, 21, 32,
          76, 54, 19, 13, 43,
          65, 87, 7, 11, 12,
          16, 22, 1, 45, 67,
          0, 23, 2, 32, 76]
meta = 25
for venda in vendas:
    if venda < meta:
        print('A loja não ganha o bônus.')
        break
    print(venda)

#Segundo exemplo usando CONTINUE:
vendas = [180, 130,150,170]
meta = 140
for venda in vendas:
    if venda < meta:
        continue
    print(venda)

#Juntando vendedores para implementar o código e usando um índice para buscar vendedores que bateram a meta.
#primeira lista do FOR.
vendedores = ["Ana", "João", "Maria", "Pedro", "Mariana", "Lucas", "Camila", "Gustavo", "Laura", "Rafael",
         "Carolina", "Rodrigo", "Isabela", "Bruno", "Lívia", "Diego", "Amanda", "Felipe", "Natália", "Alexandre",
         "Letícia", "Marcelo", "Juliana", "Thiago", "Fernanda", "Daniel", "Patrícia", "Henrique", "Sara", "Ricardo"]
meta = 25
print('Bateram a meta: ')
for i,venda in enumerate(vendas):
    if venda > meta:
        print(vendedores[i])
