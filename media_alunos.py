#Calculando média, e verificando alunos acima da média.
#Percorrendo listas com For e usando verificações condicionais.
alunos = ["José", "Joana", "Maria", "Carla", "Mauricio", "Andre", "Tiago", "Enzo", "Amanda", "Alessandra"]
notas = [
    [10, 9, 8, 8],
    [9, 7, 6, 4],
    [10, 10, 10, 10],
    [5, 3, 10, 9],
    [7, 6, 6, 6],
    [7, 7, 8, 7],
    [7, 7, 7, 9],
    [8, 5, 6, 7],
    [10, 9, 7, 4],
    [10, 1, 3, 3],
]

qtd_acima_media = 0
for i, aluno in enumerate(alunos):
    #print(notas[i])
    media_aluno = sum(notas[i])/len(notas[i])
    #print(media_aluno)

    if media_aluno >= 7:
        print(f'{aluno} tem a media de {media_aluno}')
        qtd_acima_media += 1
print(f'A quantidade acima da media foi de {qtd_acima_media} alunos.')