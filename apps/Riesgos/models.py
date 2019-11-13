import datetime

from django.db import models
from django.contrib.auth.models import User


# Create your models here.
# Modelo que permite crear la tabla Riesgo en la base de datos
# id: cadena que identifica a un riesgo
# nombre: nombre del riesgo
# models.Model: instancia del modelo


class Riesgo(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return '{} {}'.format(self.nombre, self.id)


# Modelo que permite crear la tabla Test en la base de datos
# id: cadena que identifica a un test
# idRiesgo: foranea que permite la relacion de uno a uno el riesgo al que pertenece
# fecha: fecha de la creacion del Test
# descripcion: introduccion de la funcionalidad del test
# estado: estado en el que se encuentra el test True o false, por defecto el True


class TestME(models.Model):
    id = models.AutoField(primary_key=True)
    idRiesgo = models.ForeignKey(Riesgo, null=False, on_delete=models.CASCADE)
    fecha = models.DateTimeField(null=False, default=datetime.datetime.now())
    descripcion = models.CharField(max_length=500, null=False, default='Riesgo Musculo Esqueletico')
    estado = models.BooleanField(default=True)
    usuario = models.ForeignKey(User, models.ForeignKey(User, null=False, on_delete=models.CASCADE))
    diagnostico = models.CharField(max_length=30, null=True)


class Cargo(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(null=False, max_length=30)
    descripcion = models.CharField(null=False, max_length=200)

    def __str__(self):
        return '{} {}'.format(self.nombre, self.id)


class Dependencia(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(null=False, max_length=30)
    descripcion = models.CharField(null=False, max_length=200)

    def __str__(self):
        return '{} {}'.format(self.nombre, self.id)


class PerfilDemografico(models.Model):
    id0 = models.AutoField(primary_key=True)
    test0 = models.OneToOneField(TestME, null=False, on_delete=models.CASCADE)
    cedula0 = models.IntegerField(null=False)
    nombre0 = models.CharField(null=False, max_length=30)
    apellido0 = models.CharField(null=False, max_length=30)
    sexo0 = models.BooleanField(null=False)
    peso0 = models.DecimalField(null=False, max_digits=5, decimal_places=2)
    manoDominante0 = models.CharField(null=False, max_length=10)
    cargo0 = models.ForeignKey(Cargo, null=False, on_delete=models.CASCADE)
    dependencia0 = models.ForeignKey(Dependencia, null=False, on_delete=models.CASCADE)
    antiguedadCargo0 = models.DecimalField(null=False, max_digits=5, decimal_places=2)
    actividadFisica0 = models.CharField(null=False, max_length=30)
    horasActividadFisi0 = models.IntegerField(null=False)
    variaSuJornada0 = models.BooleanField(null=False)


# Modelo de la tabla en la que se guardan los datos de los desordenes musculo esqueleticos
# usuario : usuario que llena los datos
# test : el test por defecto es el musculo esqueletico ME valor:1
# lugarMolestia: 1 lado izquierdo 2 lado derecho 3 ambos
# laMolestiaEs: 1 Dolor 2 hormigueo 3 malestar 4 adormecimiento
# molestiaSepresenta: 1 al realizar mi trabajo 2 todo el tiempo 3 al final del dia 4 al final de la semana 5 en mi casa
# seEfectuaMolestia: 1 si realizo movimientos con el hombro hacia delante 2 si realizo movimientos con el hombro hacia atras
# intensidadMolestia: 1 a 10 que tanto dolor siente la persona
# otraActividadMolestaAu: 1 si 2 no
# otraActividadMolestaDis: 1 si 2 no
# duracionMolestia: 1 menos de dos horas 2 mas de dos horas 3 intermitente durante el dia 4 constante todo el dia
# interfirioTrabajo: 1 no 2 poca interferencia 3 interferencia sustancialmente

class HombroME(models.Model):
    id1 = models.AutoField(primary_key=True)
    test1 = models.OneToOneField(TestME, null=False, on_delete=models.CASCADE)
    lugarMolestia1 = models.IntegerField(null=True)
    molestiaSepresenta1 = models.IntegerField(null=True)
    laMolestiaEs1 = models.IntegerField(null=True)
    seEfectuaMolestia1 = models.IntegerField(null=True)
    intensidadMolestia1 = models.IntegerField(null=True)
    otraActividadMolestaAu1 = models.IntegerField(null=True)
    otraActividadMolestaDis1 = models.IntegerField(null=True)
    duracionMolestia1 = models.IntegerField(null=True)
    interfirioTrabajo1 = models.IntegerField(null=True)


class CuelloME(models.Model):
    id2 = models.AutoField(primary_key=True)
    test2 = models.OneToOneField(TestME, null=False, on_delete=models.CASCADE)
    lugarMolestia2 = models.IntegerField(null=True)
    molestiaSepresenta2 = models.IntegerField(null=True)
    laMolestiaEs2 = models.IntegerField(null=True)
    seEfectuaMolestia2 = models.IntegerField(null=True)
    intensidadMolestia2 = models.IntegerField(null=True)
    otraActividadMolestaAu2 = models.IntegerField(null=True)
    otraActividadMolestaDis2 = models.IntegerField(null=True)
    duracionMolestia2 = models.IntegerField(null=True)
    interfirioTrabajo2 = models.IntegerField(null=True)


class CodoME(models.Model):
    id3 = models.AutoField(primary_key=True)
    test3 = models.OneToOneField(TestME, null=False, on_delete=models.CASCADE)
    lugarMolestia3 = models.IntegerField(null=True)
    molestiaSepresenta3 = models.IntegerField(null=True)
    laMolestiaEs3 = models.IntegerField(null=True)
    seEfectuaMolestia3 = models.IntegerField(null=True)
    intensidadMolestia3 = models.IntegerField(null=True)
    otraActividadMolestaAu3 = models.IntegerField(null=True)
    otraActividadMolestaDis3 = models.IntegerField(null=True)
    duracionMolestia3 = models.IntegerField(null=True)
    interfirioTrabajo3 = models.IntegerField(null=True)


class ManoME(models.Model):
    id4 = models.AutoField(primary_key=True)
    test4 = models.OneToOneField(TestME, null=False, on_delete=models.CASCADE)
    lugarMolestia4 = models.IntegerField(null=True)
    molestiaSepresenta4 = models.IntegerField(null=True)
    laMolestiaEs4 = models.IntegerField(null=True)
    seEfectuaMolestia4 = models.IntegerField(null=True)
    intensidadMolestia4 = models.IntegerField(null=True)
    otraActividadMolestaAu4 = models.IntegerField(null=True)
    otraActividadMolestaDis4 = models.IntegerField(null=True)
    duracionMolestia4 = models.IntegerField(null=True)
    interfirioTrabajo4 = models.IntegerField(null=True)


class EspaldaBajaME(models.Model):
    id5 = models.AutoField(primary_key=True)
    test5 = models.OneToOneField(TestME, null=False, on_delete=models.CASCADE)
    lugarMolestia5 = models.IntegerField(null=True)
    molestiaSepresenta5 = models.IntegerField(null=True)
    laMolestiaEs5 = models.IntegerField(null=True)
    seEfectuaMolestia5 = models.IntegerField(null=True)
    intensidadMolestia5 = models.IntegerField(null=True)
    otraActividadMolestaAu5 = models.IntegerField(null=True)
    otraActividadMolestaDis5 = models.IntegerField(null=True)
    duracionMolestia5 = models.IntegerField(null=True)
    interfirioTrabajo5 = models.IntegerField(null=True)


class EspaldaDorsalME(models.Model):
    id6 = models.AutoField(primary_key=True)
    test6 = models.OneToOneField(TestME, null=False, on_delete=models.CASCADE)
    lugarMolestia6 = models.IntegerField(null=True)
    molestiaSepresenta6 = models.IntegerField(null=True)
    laMolestiaEs6 = models.IntegerField(null=True)
    seEfectuaMolestia6 = models.IntegerField(null=True)
    intensidadMolestia6 = models.IntegerField(null=True)
    otraActividadMolestaAu6 = models.IntegerField(null=True)
    otraActividadMolestaDis6 = models.IntegerField(null=True)
    duracionMolestia6 = models.IntegerField(null=True)
    interfirioTrabajo6 = models.IntegerField(null=True)


class SabiasQue(models.Model):
    id = models.AutoField(primary_key=True)
    idRiesgo = models.ForeignKey(Riesgo, null=False, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100, null=False)
    descripcion = models.CharField(max_length=500, null=False)
    demostracion = models.ImageField(upload_to='demostraciones', null=True)


class PosibleEnfermedad(models.Model):
    id = models.AutoField(primary_key=True)
    idRiesgo = models.ForeignKey(Riesgo, null=False, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100, null=False)
    descripcion = models.CharField(max_length=400, null=False)

    def __str__(self):
        return '{}'.format(self.nombre)


class DefinicionEnfermedad(models.Model):
    id = models.AutoField(primary_key=True)
    enfermedad = models.ForeignKey(PosibleEnfermedad, null=False, on_delete=models.CASCADE)
    descripcion1 = models.CharField(null=False, max_length=400)
    imagen = models.ImageField(upload_to='photo', null=True)


class poblacion(models.Model):
    identificacion = models.AutoField(primary_key=True)
    correo = models.EmailField(max_length=100, null=False, blank=True, unique=True)
    Riesgo = models.ForeignKey(Riesgo, on_delete=models.CASCADE)

    def __str__(self):
        return '{} {} {}'.format(self.correo, self.identificacion, self.Riesgo)
