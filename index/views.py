from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse

def inicio(request):
    return render(request,"index/index.html")

def Año(request,numero):
    resultado = 2022 - numero
    return HttpResponse(f"<h1>Naciste en el año: {resultado}</h1>") 

def Plantilla(request):
    # Forma Vieja
    # direccion = open(r"C:\Users\campo\OneDrive\Escritorio\Proyecto Final Python\Templates\template.html")
    # template = Template(direccion.read())
    
    # Forma con loader
    # template = loader.get_template("template.html")
    # plantilla_preparada = template.render(diccionario_de_datos)
    # return HttpResponse(plantilla_preparada)

    # Forma con Render
    return render(request, "index/template.html")
