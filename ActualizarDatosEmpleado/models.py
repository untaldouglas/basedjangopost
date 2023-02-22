from django.db import models

# Create your models here.
class Empleado(models.Model):
    id = models.AutoField(primary_key=True)
    nombres = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    
    GENERO =(
        ('MASCULINO','Masculino'),
        ('FEMENINO','Femenino')
    )
    genero = models.CharField(max_length=10, choices=GENERO)
    fecha_nacimiento = models.DateField()
    email = models.EmailField()

