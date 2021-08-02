# crear una funcion que me permita repetir una cadena de texto
def repetirCadenatexto(t : str):
    tex_r = t + " "+ t
    print(tex_r)

#repetirCadenatexto('ciclo uno fundamentos')

# crear una funcion sin parametros
def imprimirMen():
    print('Grupo 39')

# llamando la funcion
#imprimirMen()

# crear una función que me retorne una cadena de texto
def imprimirMen_r():
    return "Grupo 39"

# llamar la funcion imprimirMen_r
#print(imprimirMen_r())

texto = imprimirMen_r()
# print(texto)

def suma(var_a, var_b):
    resultado = var_a + var_b
    return resultado

#print(suma(12,8))

def resta(var_c, var_d):
    resultado = var_c - var_d
    return resultado

# print(resta(30,45))

def repetirOpe():
    print(suma(12,4))
    print(suma(32,14))
    print(resta(17,21))
    print(resta(32,10))

repetirOpe()