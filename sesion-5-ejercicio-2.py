# Escribe una función que pueda decirte si un número (número entero) es primo o no.

def esPrimo(numero):
    if numero % 2 == 0:
        return 'No es primo'
    else:
        return 'Es primo'

print(esPrimo(17))