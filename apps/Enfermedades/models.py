from django.db import models

# Create your models here.
class Enfermedad(models.Model):
    identificador =  models.CharField(primary_key=True, max_length=10)
    titulo = models.CharField(max_length=100)
    definicion = models.TextField()
    fecha = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.titulo

    def def_corta(self):
        return self.definicion[:50]



