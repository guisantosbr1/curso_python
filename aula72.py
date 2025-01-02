def multiplicar(*args):
    resultado = 1
    for numero in args:
        resultado *= numero
    return resultado


multiplicacao = multiplicar(10, 2,3,4,5)
print(f"O resultado da multiplicação é: {multiplicacao}")


def par_ou_impar(numero):
    multiplo_de_dois = numero % 2 == 0
    if multiplo_de_dois:
        return f'{numero} é par'
    return f'{numero} é ímpar'


print(par_ou_impar(2))
print(par_ou_impar(5))
print(par_ou_impar(72))
print(par_ou_impar(18)) 