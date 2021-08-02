def calcular_tarifa_taxi(kilometrosRecorridos: float)->int:
    precio=4000
    metros=kilometrosRecorridos*1000
    precio=precio+(82*metros)/100
    return "Total a pagar es: "+ str(precio)
    
print(calcular_tarifa_taxi(2))