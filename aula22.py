# and (e) or (ou) not (não)

# entrada = input('[E]ntrar [S]air: ')
# senha_digitada = input('Senha: ')
# senha_permitida = '123'

# if (entrada == 'E' or entrada == 'e') and senha_digitada == senha_permitida:
#     print('Entrar')
# else:
#     print('Sair')

senha = input('Senha: ') or ('Sem senha')
print(senha)