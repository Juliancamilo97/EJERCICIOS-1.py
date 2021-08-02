# crear diccionario con el nombre y apellido
informacion_dict = {'Nombre': 'Cristian','Apellido':'Sanchez'}

def mostra_nom_completo(info_d : dict)-> str:
    #return "el nombre completo es : " + info_d['Nombre'] + " " + info_d['Apellido']
    return "el nombre completo es {} {}". format(info_d['Nombre'], info_d['Apellido']) 

print(mostra_nom_completo(informacion_dict))