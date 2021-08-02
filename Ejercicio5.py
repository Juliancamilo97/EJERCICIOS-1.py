nota1 = 3.4 # primera nota
nota2 = 4
nota3 = 2.6
nota4 = 4.7

promedio = ((nota1 + nota2 + nota3 + nota4)/4)

print(promedio)

def cal_promedio(n1,n2,n3,n4):
    result = ((n1 + n2 + n3 + n4)/4)
    result = round(result,3)
    # return "el promedio de las notas es : " + str(result)
    return "el promedio de las notas es : " + str(result)


print(cal_promedio(nota1, nota2, nota3, nota4))


def cal_promedio_tu(list_notas):
    result = (sum(list_notas)/len(list_notas))
    return result

notas = (3.4,4,2.6,4.7)
notas_antes = (3.4,4,2.6,4.7,2.5)

mi_result_tu = cal_promedio_tu(notas_antes)
print(mi_result_tu)
print(type(notas))