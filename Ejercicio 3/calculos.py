def suma(a, b):
    """
        Esta función recibe dos números como parámetros y devuelve la suma de ambos.
    """
    return a + b

def resta(a, b):
    """
        Esta función recibe dos números como parámetros y devuelve la resta de ambos.
    """
    return a - b

def multiplicacion(a, b):
    """ 
        Esta función recibe dos números como parámetros y devuelve la multiplicacion de ambos.
    """
    return a * b

def division(a, b):
    """
        Esta función recibe dos números como parámetros y devuelve la division de ambos, si es divisible por cero muestra un error.
    """
    if b == 0:
        raise ValueError("No se puede dividir por cero")
    return a / b
