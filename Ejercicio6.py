def con_nombre_genero(letra_genero): 
    pass  # no se realiza 
    # return letra_genero

type(con_nombre_genero)
print(con_nombre_genero("M"))


def multiplicar(var_a : int, var_b : int)-> int:
    result = (var_a * var_b)
    return result

rta = multiplicar(14, 3)
print(rta)

def division(var_x, var_y)->str:
    result = str(round((var_x / var_y),2))
    return result

rta_d = division(50, 7)
print("la division de las variables x y es :" + rta_d)


def otra_suma(numero1,numero2):
    print(numero1 + numero2)
    print("\n")
    return numero1 + numero2

resultado = otra_suma(5,6)
print(resultado)