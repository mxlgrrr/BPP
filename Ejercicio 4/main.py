import pdb

# Ejercicio 1
lista = [[2, 4, 1], [1,2,3,4,5,6,7,8], [100,250,43]]
pdb.set_trace()
maximos = [max(sublista) for sublista in lista]
print(maximos)

# Ejercicio 2
def es_primo(num):
    for n in range(2, num):
        if num % n == 0:
            return False
    return True

numeros = [3, 4, 8, 5, 5, 22, 13]
primos = list(filter(es_primo, numeros))
print(primos)