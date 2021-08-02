# import math as m
# declaramos una variable de tipo entero
var_int = 50

# declaramos una variable de tipo float, dooble
var_pi = 3.1416

# declaramos una variable de tipo cadena de texto o (String)
var_str = " Grupo 37"

# declaramos una variable de tipo boolean
var_boo = False

# crear variable de diccionario 
var_dict = {
    "nombre":"Juliana", 
    "apellido": "Correa",
    "edad": 37
}
# obtener o modificarlo el valor de un campo del diccionario
var_dict["nombre"] = "Maria"
# agregar nuevo campo al diccionario
var_dict["peso"] = 57.4
# eliminar un campo del diccionario
var_dict.pop('apellido')


#print("el nombre de la persona es " + var_dict["nombre"] + " y tiene " + str(var_dict["edad"]))
#print("el nombre de la persona es " + var_dict["nombre"] + " y tiene ", var_dict["edad"])
#print(f"el nombre de la persona es {var_dict['nombre']} y su edad es de {var_dict['edad']}")
#print("el nombre de la persona es {} y su edad es de {}". format(var_dict['nombre'],var_dict['edad']))
print(var_dict)


''' tres comillas sencillas
print(type(var_int))
print(type(var_str))
print(type(var_boo))
print(type(var_dict))
print(var_dict['nombre'])
'''

# print(m.pi)