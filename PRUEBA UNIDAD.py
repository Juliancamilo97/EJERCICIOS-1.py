'''
def alquiler(kilometros: float)->str:
    precio=0
    if kilometros <= 300:
        precio = 300000
    if 300 < kilometros <= 1000:
        precio = 300000 + 15000*(kilometros-300)
    if kilometros > 1000:
        precio = 300000 + 10000*(kilometros-300) 
    iva= precio*0.16    
    print('El monto a pagar es de ' + str(int(precio)) + ' y el iva es de '+ str(iva))
    return precio

alquiler(float(input("¿Cuál es la cantidad de kilometros recorrida?: ")))
'''
def alquiler(kilometros: float)->str:
    precio=0
    if 0< kilometros <= 300:
        precio = 300000
    if 300 < kilometros <= 1000:
        precio = 300000 + 15000*(kilometros-300)
    if kilometros > 1000:
        precio = 300000 + 10000*(kilometros-300) 
    iva= precio*0.16    
    return 'El monto a pagar es de ' + str(int(precio)) + ' y el iva es de '+ str(iva)

print(alquiler(301))
print(alquiler(1125))
