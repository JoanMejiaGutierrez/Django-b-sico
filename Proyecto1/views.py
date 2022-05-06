from xmlrpc.client import DateTime
from django.http import HttpResponse
import datetime


#Las vistas saludo y despedida son estaticas ya que no cambia ningun valor en la ejecución
def saludo(request):
    documentoSaludo = """
    <html>
        <body>
            <H1>Hola, Esta es una prueba de django </H1>
        </body>
    </html>
    """
    return HttpResponse(documentoSaludo)

def despedida(request):
    documentoAdios = """
    <html>
        <body>
            <H1>Adios </H1>
        </body>
    </html>
    """
    return HttpResponse(documentoAdios)



#La vista obtenerFecha es dinamica ya que cambia durante la ejecución

def obtenerFecha(request):
    fechaActual = datetime.datetime.now()
    docObtenerFecha = """
    <html>
        <body>
            <H2>
                Fecha y hora actuales: %s
            </H2>
        </body>
    </html>
    """ %fechaActual
    #s es un marcador de posición de python y en esa posición se coloca el valor de fechaActual
    return HttpResponse(docObtenerFecha)


def calcularEdad(request, ano, edad): #parametro adicional que representa el año
    periodo = ano - 2022
    edadFutura = edad + periodo
    doc = """
    <html>
        <body>
            <H2>En el año %s tendrás %s años</h2>
        </body>
    </html>
    """%(ano, edadFutura)#Esta cadena cuenta con 2 marcadores de posición para año y edad futura respectivamente

    return HttpResponse(doc)