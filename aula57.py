salas = [

    ['Maria', 'Helena'], #0

    ['Guilherme'], #1


    ['Matheus', 'Flavia', 'João'],  #2


]

##print(salas[0][1])
##print(salas[2][3][2])


for sala in salas:
    print(f'A sala é {sala}')
    for aluno in sala:
        print(aluno)