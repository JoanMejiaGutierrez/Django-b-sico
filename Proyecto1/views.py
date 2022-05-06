from django.http import HttpResponse

def saludo(request):
    return HttpResponse("Hola alumno esta es nuestra pagina en django")

def despedida(request):
    return HttpResponse("Adios")