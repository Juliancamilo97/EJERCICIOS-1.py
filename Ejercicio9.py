def costo_tiquetes(primeraclase: int, segundaclase: int, terceraclase:int)->str:
    precio1=480000
    precio2=300000
    precio3=190000
    costo= (primeraclase*precio1)+(segundaclase*precio2)+(terceraclase*precio3)
    return 'El costo total de los tiquetes es '+ str(costo)

print(costo_tiquetes(3,10,9))
print(costo_tiquetes(1,7,2))