from django.shortcuts import render

def home(request):
  return render(request, 'home.html', {})

def usoDinamico(request, id, nombre, apellido, edad):
  # este es el contexto
  data = {
    "id": id,
    "nombre": nombre,
    "apellido": apellido,
    "edad": edad
  }
  return render(request, 'usoDinamico.html', data)