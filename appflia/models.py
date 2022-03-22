from django.db import models

class Familia(models.Model):
    id = models.IntegerField(primary_key = True)
    nombre = models.CharField(max_length = 20)
    apellido = models.CharField(max_length = 40)
    fecha_nacimiento = models.DateField()
    altura = models.FloatField()
