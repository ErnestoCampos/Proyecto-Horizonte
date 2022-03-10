from django.template import loader
from django.http import HttpResponse


def Año(request,numero):
    resultado = 2022 - numero
    return HttpResponse(f"<h1>Naciste en el año: {resultado}</h1>") 

def Plantilla(request):
    # direccion = open(r"C:\Users\campo\OneDrive\Escritorio\Proyecto Final Python\Templates\template.html")
    # template = Template(direccion.read())


    template = loader.get_template("template.html")

    nombre = 'Robinson Crusoe'
    apellido = 'Campos'
    
    lista = [3,1,2,45,1,2,3]
    
    diccionario_de_datos = {
        'nombre': nombre,
        'apellido': apellido,
        'edad': 17,
    }

    
    plantilla_preparada = template.render(diccionario_de_datos)
    
    return HttpResponse(plantilla_preparada)