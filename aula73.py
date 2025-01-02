def saudacao(msg, nome):
    return f'{msg}, {nome}!'

def executar(funcao, *args):
    return funcao(*args)

print(
    executar(saudacao, 'Olá', 'Maria')
)
print(executar(saudacao, 'Oi', 'João')
)