from django.http import HttpResponse
from django.shortcuts import render

from .models import Pregunta, Respuesta, Cuestionario
from .mach import modelo

#model= SentenceTransformer('paraphrase-multilingual-MiniLM-L12-v2')

#print("Para que el modelo funcione correctamente tienes que respondes a las preguntas con frases y evitar los monosílabos")


def funct(request, id):
    if id< 22 :
        pregunta = Pregunta.objects.filter(id=id).values()#devuelve un objeto, la fila de la base de datos
        pregunta = pregunta[0]["pregunta"]#le digo que me coja solo la parte de la pregunta de la base de datos
        siguiente = id+1
    
    if request.method == "GET":
        #resultado = modelo(id, respuesta)
        #id += 1
        return render(request, "core/main.html", {'id': id, 'siguiente': siguiente, 'pregunta': pregunta})#devuelve el template
    else:
        
        resp=request.POST["respuestahtml"]
        puntuacion=modelo(id -1, resp)
        print("puntuacion:", puntuacion)
        guardado=Respuesta(id -1,puntuacion)
        guardado.save()
        
        if id==22 :
            sumatorio=0
            aux=Respuesta.objects.all()
            for i in aux:
                sumatorio += i.respuesta
            return render(request, "core/final.html", {'sumatorio': sumatorio})#devuelve el template
        return render(request, "core/main.html", {'id': id, 'siguiente': siguiente, 'pregunta': pregunta})#devuelve el template

# la funcion resultados es para testear el template final
def resultados(request):

    #sumatorio=45
    return render(request, "core/final.html", {'sumatorio': sumatorio})#devuelve el template

def inicio(request):
    borrado=Respuesta.objects.all()
    borrado.delete()
    return render(request,"core/inicio.html")

def cuestionario(request, respuesta):
    if respuesta =="si" :
        guardar=Cuestionario(si = 1)
        guardar.save()

    else :
        guardar=Cuestionario(no = 1)
        guardar.save()

    auxsi = Cuestionario.objects.filter(si=1).count()
    auxno = Cuestionario.objects.filter(no=1).count()
    auxtotal=auxsi+auxno
    auxsi=auxsi/auxtotal*100
    auxno=auxno/auxtotal*100
    return render(request, "core/cuestionario.html", {'respuesta': respuesta, 'auxsi':auxsi , 'auxno': auxno})

