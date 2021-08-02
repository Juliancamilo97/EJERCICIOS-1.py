# declarar variable float
var1 = 1.20
#print(var1)
# castiar variable de float a entero
var1 = int(var1)
#print(var1)

''' 
  errores al inicilizar variable
var 1 = 10
@var = 20
1var = 30
var-1 = 40
'''

num1 = num2 = num3 = 200
num_x1, num_x2, num_x3 = 10,85,4.6

#print(num3)
#print(num_x3)


'''
+ suma
- resta
* multiplicacion
/ division
// division entero
** potencia
() parentesis
'''

nota1 = 3.4 # primera nota
nota2 = 4
nota3 = 2.6
nota4 = 4.7


promedio = ((nota1 + nota2 + nota3 + nota4)/4)
promedio_fsum = (sum((nota1,nota2,nota3,nota4))/4)
nota_max = max(nota1,nota2,nota3,nota4)
nota_min = min(nota1,nota2,nota3,nota4)

'''
print(promedio_fsum)
print(round(promedio_fsum,1))
print(nota_max)
print(nota_min)
help(print)
'''


# print(int("2021"))
# print(4**(1/2))

#len cuenta cuantos elementos tiene la cadena de texto o el array
x = range(10,100)
print(len(x))

texto = 'Ciclo 1, Fundamentos de programación'
print(len(texto))
