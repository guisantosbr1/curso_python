p1 = {
    'nome': 'Guilherme',
    'sobrenome': 'Santos',
}

#print(p1['nome'])
#print(p1.get('nome', 'Não existe'))
# p1.update ({
#     'nome': 'Cristiano',
#     'idade': 39
# })
p1.update(nome='Cristiano', idade=39)
print(p1)