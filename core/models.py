from django.db import models

# Create your models here.
class Pregunta(models.Model):
    pregunta= models.CharField(max_length=180)
    respuesta1= models.CharField(max_length=120)
    respuesta2= models.CharField(max_length=120)
    respuesta3= models.CharField(max_length=120)
    respuesta4= models.CharField(max_length=120)

class Respuesta(models.Model):
    respuesta = models.DecimalField(max_digits=5, decimal_places=3)

class Cuestionario(models.Model):
    si= models.IntegerField(null=True)
    no= models.IntegerField(null=True)