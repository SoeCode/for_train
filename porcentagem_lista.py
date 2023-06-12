# 1. Calculando % de uma lista
#Calculando porcentagem de vendedores que bateram a meta de duas maneiras diferentes.
#No final, buscando qual vendedor e qual quantidade vendida do maior numero de vendas.
meta = 10000
vendas = [
    ['Gabriel', 15000],
    ['Julia', 27000],
    ['Nicolas', 9900],
    ['Maria', 3750],
    ['Ana', 10300],
    ['Alison', 37870],
    ['Lidia', 3400],
    ['Fred', 19000],
    ['Clo', 2300],
]
#metodo 1
bateu_meta = []
for venda in vendas:
    #print(venda[1])
    if venda[1] > meta:
        bateu_meta.append(venda)
        
print(f'{len(bateu_meta)/len(vendas):.1%} dos vendedores bateram a meta.')
#-------------------------------------------------------------------------
#metodo 2
qtde_bateu_meta = 0
for venda in vendas:
    #print(venda[1])
    if venda[1] > meta:
        qtde_bateu_meta += 1
print(qtde_bateu_meta)
print(f'{qtde_bateu_meta/len(vendas):.1%} Bateram a meta.')
#-------------------------------------------------------------------------
#Vendedor que mais vendeu:
vend_mais_vendeu = ''
qtd_mais_vendida = 0
for venda in vendas:
    #print(venda[1])
    if venda[1] > qtd_mais_vendida:
        qtd_mais_vendida = venda[1]
        vend_mais_vendeu = venda[0]
print(f'{vend_mais_vendeu} foi quem mais vendeu. Com um total de {qtd_mais_vendida:,} unidades.')