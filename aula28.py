nome = input('Digite seu nome aqui: ')
idade = int(input('Digite sua idade aqui: '))

if nome and idade:
    print(f'Seu nome é: {nome}')
    print(f'Seu nome invertido é: {nome[::-1]}')

    if ' ' in nome:
        print('Seu nome TEM espaços')
    else:
        print('Seu nome NÃO tem espaços')

    print(f'Seu nome tem: {len(nome)} letras ')
    print(f'A primeira letra do seu nome é: {nome[0]}')
    print(f'A última letra do seu nome é: {nome[-1]}')