#Três listas: produtos, vendas2019 e vendas2020. Cada uma dessas listas contém informações sobre produtos e vendas correspondentes aos anos de 2019 e 2020.
#Percorrendo a lista produtos e obtendo o índice i e o valor produto em cada iteração.
#Por fim, exibindo o nome do produto, a quantidade de unidades vendidas em 2020 e o crescimento percentual em relação ao ano anterior.


produtos = ['iphone', 'galaxy', 'ipad', 'tv', 'máquina de café', 'kindle', 'geladeira', 'adega', 'notebook dell', 'notebook hp', 'notebook asus', 'microsoft surface', 'webcam', 'caixa de som', 'microfone', 'câmera canon']
vendas2019 = [558147,712350,573823,405252,718654,531580,973139,892292,422760,154753,887061,438508,237467,489705,328311,591120]
vendas2020 = [951642,244295,26964,787604,867660,78830,710331,646016,694913,539704,324831,667179,295633,725316,644622,994303]
#seu código aqui
for i, produto in enumerate(produtos):
    if vendas2019[i] < vendas2020[i]:
        #print(vendas2020[i])
        crescimento = vendas2020[i] / vendas2019[i] - 1
        print(f'{produtos[i]} vendeu {vendas2020[i]} unidades. Um crescimento de {crescimento:.1%} em relação ao ano anterior.')


