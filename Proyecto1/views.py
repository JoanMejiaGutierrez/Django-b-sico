from multiprocessing import context
from pipes import Template
from pydoc import doc
from re import TEMPLATE, template
from xmlrpc.client import DateTime
import django
from django.http import HttpResponse
import datetime
from django.template import Template, Context


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


def Mostrar_Mi_Primer_Plantilla(request):

    nombre = "Miguel Angel"
    apellido = "Gerrero"
    fecha_actual = datetime.datetime.now()

    miPersona1 = Persona("Joan", "Mejia")#Probamos enviar las propiedades de un parametro
    #con open() no es la forma mas recomendable si no con cargadores
    #doc_externo = open("C:/Users/Joan/Desktop/Proyectos Django/Proyecto1/Proyecto1/Plantillas/miPrimerPlantillas.html") #metodo para cargar elementos externos donde obtiene todo el codigo de la plantilla
    doc_externo = open("C:/Users/Joan/Desktop/Proyectos Django/Proyecto1/Proyecto1/Plantillas/miPrimerPlantillas.html")
    plltlla = Template(doc_externo.read())#carga la plantilla
    doc_externo.close()

    ctx = Context({"nombre_persona": nombre, "apellido_persona": apellido, "momento_actual": fecha_actual, "miPNombre": miPersona1.nombre, "miPApellido": miPersona1.apellido, "miP": miPersona1})#enviamos parametros por diccionario

    documento = plltlla.render(ctx)#renderiza o muestra el contenido en pantalla

    return HttpResponse(documento)



class Persona(object):
    def __init__(self, nombre, apellido) -> None:
        self.nombre = nombre
        self.apellido = apellido