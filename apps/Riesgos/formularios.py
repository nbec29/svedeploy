from django.forms import CheckboxSelectMultiple

from apps.Riesgos.models import  poblacion, PerfilDemografico, HombroME,TestME, CuelloME,ManoME,CodoME,EspaldaDorsalME,\
    EspaldaBajaME, PosibleEnfermedad,DefinicionEnfermedad,SabiasQue
from django import forms
from django.contrib.auth import  get_user
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm





class EnfermedadForm(forms.ModelForm):

    class Meta:
        model = PosibleEnfermedad

        fields = [
            
            'idRiesgo',
            'nombre',
            'descripcion',


        ]
        labels ={
           
            'idRiesgo': 'Riesgo',
            'nombre':'Nombre',
            'descripcion':'Descripción',
        }
        widgets = {

            
            'idRiesgo':forms.Select(attrs={'class': 'form-control'}),
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control'}),
        }

class DescripcionEnfermedadForm(forms.ModelForm):

    class Meta:
        model = DefinicionEnfermedad

        fields = [
            'enfermedad',
            'descripcion1',
            'imagen',
        ]
        labels ={
            'enfermedad': 'Seleccione la enfermedad',
            'descripcion1': 'Ingrese una descripción',
            'imagen':'Ingrese una imagen', 
        }
        widgets = {

            
            'enfermedad':forms.Select(attrs={'class': 'form-control'}),
            'descripcion1': forms.Textarea(attrs={'class': 'form-control'}),
            
        }


class DescripcionRecomendacionesForm(forms.ModelForm):

    class Meta:
        model = SabiasQue

        fields = [
            'idRiesgo',
            'nombre',
            'descripcion',
            'demostracion',
        ]
        labels ={
            'idRiesgo': 'Seleccione el riesgo al que pertenece',
            'nombre': 'Ingrese un nombre',
            'descripcion':'Ingrese una descripción', 
            'demostracion':'Ingrese una imagen',
        }
        widgets = {

            'idRiesgo':forms.Select(attrs={'class': 'form-control'}),
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control'}),
            
            
        }
        
        
        
        
       

class PoblacionForm(forms.ModelForm):

    class Meta:
        model = poblacion

        fields = [
            'correo',
            'Riesgo',

        ]
        labels ={
            'correo': 'Ingrese el correo:',
            'Riesgo': 'Población:',
        }
        widgets = {

            'correo': forms.TextInput(attrs={'class': 'form-control'}),
            'Riesgo':forms.Select(attrs={'class': 'form-control'}),
        }


"""formulario para el perfil demografico, permite crear la clase de el formulario para el ingreso de los datos"""
class PerfilDemograficoForm(forms.ModelForm):

    class Meta:
        model = PerfilDemografico
        exclude = ()

        fields = [
            'cedula0',
            'nombre0',
            'apellido0',
            'sexo0',
            'peso0',
            'manoDominante0',
            'cargo0',
            'dependencia0',
            'antiguedadCargo0',
            'actividadFisica0',
            'horasActividadFisi0',
            'variaSuJornada0',
            'test0',

        ]

        labels ={
            'cedula0': 'Ingrese el numero de cedula "CC" ',
            'nombre0': 'Ingrese sus nombres',
            'apellido0': 'Ingrese sus apellidos',
            'sexo0': 'Sexo',
            'peso0': 'Peso',
            'manoDominante0': '¿Cúal es su mano dominante?',
            'dependencia0': 'Elija la dependencia a la que se asocia en la universidad',
            'cargo0': ' su Cargo en la universidad del Quindío es',
            'antiguedadCargo0': 'Antiguedad en el cargo (en años)',
            'actividadFisica0': '¿ Realiza actividad física ?',
            'horasActividadFisi0': '¿Cuántas horas por día?',
            'variaSuJornada0': '¿ la duracion semanal de la jornada es variable ? ',
            'test0': 'ingrese en test ',

        }
        widgets = {

            'cedula0': forms.NumberInput(attrs={'class': 'form-control'}),
            'nombre0':forms.TextInput(attrs={'class': 'form-control'}),
            'apellido0': forms.TextInput(attrs={'class': 'form-control'}),
            'sexo0': forms.NullBooleanSelect(attrs={'class': 'form-control'}),
            'peso0': forms.NumberInput(attrs={'class': 'form-control'}),
            'manoDominante0': forms.TextInput(attrs={'class': 'form-control'}),
            'dependencia0': forms.Select(attrs={'class': 'form-control'}),
            'cargo0': forms.Select(attrs={'class': 'form-control'}),
            'antiguedadCargo0': forms.NumberInput(attrs={'class': 'form-control'}),
            'actividadFisica0': forms.NullBooleanSelect(attrs={'class': 'form-control'}),
            'horasActividadFisi0': forms.NumberInput(attrs={'class': 'form-control'}),
            'variaSuJornada0': forms.NullBooleanSelect(attrs={'class': 'form-control'}),
            'test0': forms.Select(attrs={'class': 'form-control'}),
        }

class HombroMEForm(forms.ModelForm):

            class Meta:
                model = HombroME
                exclude = ()

                fields = [
                    'test1',
                    'lugarMolestia1',
                    'molestiaSepresenta1',
                    'laMolestiaEs1',
                    'seEfectuaMolestia1',
                    'intensidadMolestia1',
                    'otraActividadMolestaAu1',
                    'otraActividadMolestaDis1',
                    'duracionMolestia1',
                    'interfirioTrabajo1',


                ]

                labels = {
                    'test1':'TEST',
                    'lugarMolestia1':'LUGAR DE LA MOLESTIA: 1 lado izquierdo 2 lado derecho 3 ambos',
                    'molestiaSepresenta1':'LA MOLESTIA SE PRESENTA COMO : 1 Dolor 2 hormigueo 3 malestar 4 adormecimiento' ,
                    'laMolestiaEs1':'LA MOLESTIA SE PRESENTA EN EL MOMENTO DE : 1 al realizar mi trabajo 2 todo el tiempo 3 al final del dia 4 al final de la semana 5 en mi casa',
                    'seEfectuaMolestia1':'LA MOLESTIA SE EFECTUA SI :_1 si realizo movimientos con el hombro hacia delante 2 si realizo movimientos con el hombro hacia atras' ,
                    'intensidadMolestia1':'QUE TAN INTENSA ES LA MOLESTIA :1 a 10 que tanta molestia siente la persona',
                    'otraActividadMolestaAu1':' ¿Siente que si realiza alguna otra actividad o la molestia o dolor Aumenta? 1 si 2 no ',
                    'otraActividadMolestaDis1':'¿Siente que si realiza alguna otra actividad o labor la molestia o dolor Disminuye? 1 si 2 no',
                    'duracionMolestia1':'Cuanto dura aproximadamente cada episodio de molestia o dolor : 1 menos de dos horas 2 mas de dos horas 3 intermitente durante el dia 4 constante todo el dia',
                    'interfirioTrabajo1':'Si usted experimentó dolor, Cuánto interfirió con su habilidad para trabajar? 1 no 2 poca interferencia 3 interferencia sustancialmente',

                }
                widgets = {


                    'test1':forms.Select(attrs={'class': 'form-control'}),
                    'lugarMolestia1': forms.NumberInput(attrs={'class': 'form-control'}),
                    'molestiaSepresenta1': forms.NumberInput(attrs={'class': 'form-control'}),
                    'laMolestiaEs1': forms.NumberInput(attrs={'class': 'form-control'}),
                    'seEfectuaMolestia1': forms.NumberInput(attrs={'class': 'form-control'}),
                    'intensidadMolestia1': forms.NumberInput(attrs={'class': 'form-control'}),
                    'otraActividadMolestaAu1': forms.NumberInput(attrs={'class': 'form-control'}),
                    'otraActividadMolestaDis1': forms.NumberInput(attrs={'class': 'form-control'}),
                    'duracionMolestia1': forms.NumberInput(attrs={'class': 'form-control'}),
                    'interfirioTrabajo1': forms.NumberInput(attrs={'class': 'form-control'}),

                }

class CuelloMEForm(forms.ModelForm):
    class Meta:
        model = CuelloME
        exclude = ()

        fields = [
            'test2',
            'lugarMolestia2',
            'molestiaSepresenta2',
            'laMolestiaEs2',
            'seEfectuaMolestia2',
            'intensidadMolestia2',
            'otraActividadMolestaAu2',
            'otraActividadMolestaDis2',
            'duracionMolestia2',
            'interfirioTrabajo2',

        ]

        labels = {
            'test2': 'TEST',
            'lugarMolestia2': 'LUGAR DE LA MOLESTIA: 1 lado izquierdo 2 lado derecho 3 ambos',
            'molestiaSepresenta2': 'LA MOLESTIA SE PRESENTA COMO : 1 Dolor 2 hormigueo 3 malestar 4 adormecimiento',
            'laMolestiaEs2': 'LA MOLESTIA SE PRESENTA EN EL MOMENTO DE : 1 al realizar mi trabajo 2 todo el tiempo 3 al final del dia 4 al final de la semana 5 en mi casa',
            'seEfectuaMolestia2': 'LA MOLESTIA SE EFECTUA SI :_1 si realizo movimientos con el cuello hacia delante 2 si realizo movimientos con el cuello hacia atras 3 movimientos hacia los lado 4 movimivientos rotativos',
            'intensidadMolestia2': 'QUE TAN INTENSA ES LA MOLESTIA :1 a 10 que tanta molestia siente la persona',
            'otraActividadMolestaAu2': ' ¿Siente que si realiza alguna otra actividad o la molestia o dolor Aumenta? 1 si 2 no ',
            'otraActividadMolestaDis2': '¿Siente que si realiza alguna otra actividad o labor la molestia o dolor Disminuye? 1 si 2 no',
            'duracionMolestia2': 'Cuanto dura aproximadamente cada episodio de molestia o dolor : 1 menos de dos horas 2 mas de dos horas 3 intermitente durante el dia 4 constante todo el dia',
            'interfirioTrabajo2': 'Si usted experimentó dolor, Cuánto interfirió con su habilidad para trabajar? 1 no 2 poca interferencia 3 interferencia sustancialmente',

        }
        widgets = {

            'test2': forms.Select(attrs={'class': 'form-control'}),
            'lugarMolestia2': forms.NumberInput(attrs={'class': 'form-control'}),
            'molestiaSepresenta2': forms.NumberInput(attrs={'class': 'form-control'}),
            'laMolestiaEs2': forms.NumberInput(attrs={'class': 'form-control'}),
            'seEfectuaMolestia2': forms.NumberInput(attrs={'class': 'form-control'}),
            'intensidadMolestia2': forms.NumberInput(attrs={'class': 'form-control'}),
            'otraActividadMolestaAu2': forms.NumberInput(attrs={'class': 'form-control'}),
            'otraActividadMolestaDis2': forms.NumberInput(attrs={'class': 'form-control'}),
            'duracionMolestia2': forms.NumberInput(attrs={'class': 'form-control'}),
            'interfirioTrabajo2': forms.NumberInput(attrs={'class': 'form-control'}),

        }

class CodoMEForm(forms.ModelForm):
    class Meta:
        model = CodoME
        exclude = ()

        fields = [
            'test3',
            'lugarMolestia3',
            'molestiaSepresenta3',
            'laMolestiaEs3',
            'seEfectuaMolestia3',
            'intensidadMolestia3',
            'otraActividadMolestaAu3',
            'otraActividadMolestaDis3',
            'duracionMolestia3',
            'interfirioTrabajo3',

        ]

        labels = {
            'test3': 'TEST',
            'lugarMolestia3': 'POSEE MOLESTIAS EN EL CODO CUANDO :: 1 extender, retraer el brazo 2 Girar el Brazo 3 ambos',
            'molestiaSepresenta3': 'LA MOLESTIA SE PRESENTA COMO : 1 Dolor 2 hormigueo 3 malestar 4 adormecimiento',
            'laMolestiaEs3': 'LA MOLESTIA SE PRESENTA EN EL MOMENTO DE : 1 al realizar mi trabajo 2 todo el tiempo 3 al final del dia 4 al final de la semana 5 en mi casa',
            'seEfectuaMolestia3': 'LA MOLESTIA SE EFECTUA SI :_1 Flexionar el brazo 2 Estirar el brazo 3 movimivientos rotativos',
            'intensidadMolestia3': 'QUE TAN INTENSA ES LA MOLESTIA :1 a 10 que tanta molestia siente la persona',
            'otraActividadMolestaAu3': ' ¿Siente que si realiza alguna otra actividad o la molestia o dolor Aumenta? 1 si 2 no ',
            'otraActividadMolestaDis3': '¿Siente que si realiza alguna otra actividad o labor la molestia o dolor Disminuye? 1 si 2 no',
            'duracionMolestia3': 'Cuanto dura aproximadamente cada episodio de molestia o dolor : 1 menos de dos horas 2 mas de dos horas 3 intermitente durante el dia 4 constante todo el dia',
            'interfirioTrabajo3': 'Si usted experimentó dolor, Cuánto interfirió con su habilidad para trabajar? 1 no 2 poca interferencia 3 interferencia sustancialmente',

        }
        widgets = {

            'test3': forms.Select(attrs={'class': 'form-control'}),
            'lugarMolestia3': forms.NumberInput(attrs={'class': 'form-control'}),
            'molestiaSepresenta3': forms.NumberInput(attrs={'class': 'form-control'}),
            'laMolestiaEs3': forms.NumberInput(attrs={'class': 'form-control'}),
            
            'seEfectuaMolestia3': forms.NumberInput(attrs={'class': 'form-control'}),
            'intensidadMolestia3': forms.NumberInput(attrs={'class': 'form-control'}),
            'otraActividadMolestaAu3': forms.NumberInput(attrs={'class': 'form-control'}),
            'otraActividadMolestaDis3': forms.NumberInput(attrs={'class': 'form-control'}),
            'duracionMolestia3': forms.NumberInput(attrs={'class': 'form-control'}),
            'interfirioTrabajo3': forms.NumberInput(attrs={'class': 'form-control'}),

        }

class ManoMEForm(forms.ModelForm):
    class Meta:
        model = ManoME
        exclude = ()
        DEDOS_MANO = ((1, 'Meñique'),
                                   (2, 'Anular'),
                                   (3, 'Corazon'),
                                   (4,'Indice'),
                                   (5,'Pulgar'))

        fields = [
            'test4',
            'lugarMolestia4',
            'molestiaSepresenta4',
            'laMolestiaEs4' ,
            'seEfectuaMolestia4',
            'intensidadMolestia4',
            'otraActividadMolestaAu4',
            'otraActividadMolestaDis4',
            'duracionMolestia4',
            'interfirioTrabajo4',


        ]
        labels = {
            'test4': 'TEST',
            'lugarMolestia4': 'POSEE MOLESTIAS EN EL MANO  : 1 lado izquierdo 2 lado derecho 3 ambos',
            'molestiaSepresenta4': 'LA MOLESTIA SE PRESENTA COMO : 1 Dolor 2 hormigueo 3 malestar 4 adormecimiento',

            'laMolestiaEs4':   'EN CASO DE PRESENCIAR MOLESTIAS, ESTAS SE PRESENTAN EN SUS DEDOS '  ,

            'seEfectuaMolestia4': 'LA MOLESTIA SE EFECTUA SI :_1 Flexionar el brazo 2 Estirar el brazo 3 movimivientos rotativos',
            'intensidadMolestia4': 'QUE TAN INTENSA ES LA MOLESTIA :1 a 10 que tanta molestia siente la persona',
            'otraActividadMolestaAu4': ' ¿Siente que si realiza alguna otra actividad o la molestia o dolor Aumenta? 1 si 2 no ',
            'otraActividadMolestaDis4': '¿Siente que si realiza alguna otra actividad o labor la molestia o dolor Disminuye? 1 si 2 no',
            'duracionMolestia4': 'Cuanto dura aproximadamente cada episodio de molestia o dolor : 1 menos de dos horas 2 mas de dos horas 3 intermitente durante el dia 4 constante todo el dia',
            'interfirioTrabajo4': 'Si usted experimentó dolor, Cuánto interfirió con su habilidad para trabajar? 1 no 2 poca interferencia 3 interferencia sustancialmente',

        }
        widgets = {

            'test4': forms.Select(attrs={'class': 'form-control'}),
            'lugarMolestia4': forms.NumberInput(attrs={'class': 'form-control'}),
            'molestiaSepresenta4': forms.NumberInput(attrs={'class': 'form-control'}),
            'laMolestiaEs4': forms.NumberInput(attrs={'class': 'form-control'}) , """ forms.NumberInput(attrs={'class': 'form-control'})      forms.MultipleChoiceField(required=False, widget=CheckboxSelectMultiple, choices=DEDOS_MANO)
            """
                         
            'seEfectuaMolestia4': forms.NumberInput(attrs={'class': 'form-control'}),
            'intensidadMolestia4': forms.NumberInput(attrs={'class': 'form-control'}),
            'otraActividadMolestaAu4': forms.NumberInput(attrs={'class': 'form-control'}),
            'otraActividadMolestaDis4': forms.NumberInput(attrs={'class': 'form-control'}),
            'duracionMolestia4': forms.NumberInput(attrs={'class': 'form-control'}),
            'interfirioTrabajo4': forms.NumberInput(attrs={'class': 'form-control'}),

        }


class EspaldaDorsalMEForm(forms.ModelForm):
    class Meta:
        model = EspaldaDorsalME
        exclude = ()

        fields = [
            'test6',
            'lugarMolestia6',
            'molestiaSepresenta6',
            'laMolestiaEs6',
            'seEfectuaMolestia6',
            'intensidadMolestia6',
            'otraActividadMolestaAu6',
            'otraActividadMolestaDis6',
            'duracionMolestia6',
            'interfirioTrabajo6',

        ]

        labels = {
            'test6': 'TEST',
            'lugarMolestia6': 'POSEE MOLESTIAS EN EL CODO CUANDO :: 1 extender, retraer el brazo 2 Girar el Brazo 3 ambos',
            'molestiaSepresenta6': 'LA MOLESTIA SE PRESENTA COMO : 1 Dolor 2 hormigueo 3 malestar 4 adormecimiento',
            'laMolestiaEs6': 'LA MOLESTIA SE PRESENTA EN EL MOMENTO DE : 1 al realizar mi trabajo 2 todo el tiempo 3 al final del dia 4 al final de la semana 5 en mi casa',
            'seEfectuaMolestia6': 'LA MOLESTIA SE EFECTUA SI :_1 Flexionar el brazo 2 Estirar el brazo 3 movimivientos rotativos',
            'intensidadMolestia6': 'QUE TAN INTENSA ES LA MOLESTIA :1 a 10 que tanta molestia siente la persona',
            'otraActividadMolestaAu6': ' ¿Siente que si realiza alguna otra actividad o la molestia o dolor Aumenta? 1 si 2 no ',
            'otraActividadMolestaDis6': '¿Siente que si realiza alguna otra actividad o labor la molestia o dolor Disminuye? 1 si 2 no',
            'duracionMolestia6': 'Cuanto dura aproximadamente cada episodio de molestia o dolor : 1 menos de dos horas 2 mas de dos horas 3 intermitente durante el dia 4 constante todo el dia',
            'interfirioTrabajo6': 'Si usted experimentó dolor, Cuánto interfirió con su habilidad para trabajar? 1 no 2 poca interferencia 3 interferencia sustancialmente',

        }
        widgets = {

            'test6': forms.Select(attrs={'class': 'form-control'}),
            'lugarMolestia6': forms.NumberInput(attrs={'class': 'form-control'}),
            'molestiaSepresenta6': forms.NumberInput(attrs={'class': 'form-control'}),
            'laMolestiaEs6': forms.NumberInput(attrs={'class': 'form-control'}),

            'seEfectuaMolestia6': forms.NumberInput(attrs={'class': 'form-control'}),
            'intensidadMolestia6': forms.NumberInput(attrs={'class': 'form-control'}),
            'otraActividadMolestaAu6': forms.NumberInput(attrs={'class': 'form-control'}),
            'otraActividadMolestaDis6': forms.NumberInput(attrs={'class': 'form-control'}),
            'duracionMolestia6': forms.NumberInput(attrs={'class': 'form-control'}),
            'interfirioTrabajo6': forms.NumberInput(attrs={'class': 'form-control'}),

        }


class EspaldaBajaMEForm(forms.ModelForm):
    class Meta:
        model = EspaldaBajaME
        exclude = ()

        fields = [
            'test5',
            'lugarMolestia5',
            'molestiaSepresenta5',
            'laMolestiaEs5',
            'seEfectuaMolestia5',
            'intensidadMolestia5',
            'otraActividadMolestaAu5',
            'otraActividadMolestaDis5',
            'duracionMolestia5',
            'interfirioTrabajo5',

        ]

        labels = {
            'test5': 'TEST',
            'lugarMolestia5': 'POSEE MOLESTIAS EN EL CODO CUANDO :: 1 extender, retraer el brazo 2 Girar el Brazo 3 ambos',
            'molestiaSepresenta5': 'LA MOLESTIA SE PRESENTA COMO : 1 Dolor 2 hormigueo 3 malestar 4 adormecimiento',
            'laMolestiaEs5': 'LA MOLESTIA SE PRESENTA EN EL MOMENTO DE : 1 al realizar mi trabajo 2 todo el tiempo 3 al final del dia 4 al final de la semana 5 en mi casa',
            'seEfectuaMolestia5': 'LA MOLESTIA SE EFECTUA SI :_1 Flexionar el brazo 2 Estirar el brazo 3 movimivientos rotativos',
            'intensidadMolestia5': 'QUE TAN INTENSA ES LA MOLESTIA :1 a 10 que tanta molestia siente la persona',
            'otraActividadMolestaAu5': ' ¿Siente que si realiza alguna otra actividad o la molestia o dolor Aumenta? 1 si 2 no ',
            'otraActividadMolestaDis5': '¿Siente que si realiza alguna otra actividad o labor la molestia o dolor Disminuye? 1 si 2 no',
            'duracionMolestia5': 'Cuanto dura aproximadamente cada episodio de molestia o dolor : 1 menos de dos horas 2 mas de dos horas 3 intermitente durante el dia 4 constante todo el dia',
            'interfirioTrabajo5': 'Si usted experimentó dolor, Cuánto interfirió con su habilidad para trabajar? 1 no 2 poca interferencia 3 interferencia sustancialmente',

        }
        widgets = {

            'test5': forms.Select(attrs={'class': 'form-control'}),
            'lugarMolestia5': forms.NumberInput(attrs={'class': 'form-control'}),
            'molestiaSepresenta5': forms.NumberInput(attrs={'class': 'form-control'}),
            'laMolestiaEs5': forms.NumberInput(attrs={'class': 'form-control'}),

            'seEfectuaMolestia5': forms.NumberInput(attrs={'class': 'form-control'}),
            'intensidadMolestia5': forms.NumberInput(attrs={'class': 'form-control'}),
            'otraActividadMolestaAu5': forms.NumberInput(attrs={'class': 'form-control'}),
            'otraActividadMolestaDis5': forms.NumberInput(attrs={'class': 'form-control'}),
            'duracionMolestia5': forms.NumberInput(attrs={'class': 'form-control'}),
            'interfirioTrabajo5': forms.NumberInput(attrs={'class': 'form-control'}),

        }


class TestMEForm(forms.ModelForm):
    class Meta:
        model = TestME

        fields = [

            'idRiesgo',
            'usuario',


        ]

        labels = {

            'idRiesgo': 'RIESGO',
            'usuario': 'USUARIO',


        }
        