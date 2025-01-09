pessoa = {}


chave = 'nome'

pessoa[chave] = 'Guilherme Santos'
pessoa['sobrenome'] = 'Costa'

print(pessoa[chave])

pessoa[chave] = 'Julia'

del pessoa['sobrenome']
print(pessoa)
print(pessoa['nome'])