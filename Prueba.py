var_int = 50
var_pi = 3.1416
var_str = " Grupo 37 "
var_boo = False
var_dict = {"nombre":"juliana", "apellido": "Correa", "edad": 37}
# Obtener o Modificar valor del campo en el diccionario
var_dict["nombre"] = "Maria"
# Agregar nuevo campo al diccionario
var_dict["peso"]=57
# Eliminar campo del diccionario
var_dict.pop('apellido')
print(var_dict)
print(type(var_int))
print(var_dict['nombre' ])
print("El nombre de la persona es " + var_dict["nombre"] + " y tiene " + str(var_dict["edad"]))
print("El nombre de la persona es " + var_dict["nombre"] + " y tiene ", var_dict["edad"])
print(var_dict)
print(f"El nombre de la persona es {var_dict['nombre']} y su edad es de {var_dict['edad']}")
print("El nombre de la persona es {} y su edad es de {}". format(var_dict['nombre'],var_dict['edad']))
