from django.http import HttpResponse

documentoSaludo = """
<html>
    <body>
        <H1>Hola, Esta es una prueba de django </H1>
    </body>
</html>
"""
documentoAdios = """
<html>
    <body>
        <H1>Adios </H1>
    </body>
</html>
"""

def saludo(request):
    return HttpResponse(documentoSaludo)

def despedida(request):
    return HttpResponse(documentoAdios)