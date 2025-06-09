from django.http import HttpResponse

def saludo(request):
    return HttpResponse("Hola mundo desde Django!")

def getuser(request, id, name):
    return HttpResponse(f"el usuario {name} tiene el id nº {id}")
    