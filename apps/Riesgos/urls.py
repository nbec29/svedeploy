from django.urls import path
from apps.Riesgos.views import inicio, riesgoME, enfermedadME, administrarSVE, PoblacionCreate, \
     Poblacionlistar, poblacionEdit, poblacionEliminar, poblacionEnviarCorreo,EnviarMensaje, \
     notificaciones, \
     iniciarTestMEPiloto
from django.contrib.auth.decorators import login_required
from django.conf.urls import url

urlpatterns = [
    path('', login_required(inicio), name='Inicio'),
    path('musculoEsqueletico', login_required(riesgoME), name='riesgoME'),
    path('musculoEsqueletico/enfermedadesME', login_required(enfermedadME), name='enfermedadesME'),
    path('musculoEsqueletico/testME/iniciarTestMEPiloto', login_required(iniciarTestMEPiloto), name='iniciarTestMEPiloto'),


    path('musculoEsqueletico/testME/enviado', login_required(EnviarMensaje), name='enfermedadesME'),
    path('administrarSVE', login_required(administrarSVE), name='administrarsve'),
    path('notificaciones', login_required(notificaciones), name='notificaciones'),
    path('administrarSVE/poblacionSVE', login_required(PoblacionCreate), name='poblacionSVE'),
    path('administrarSVE/poblacionSVE/lista', login_required(Poblacionlistar), name='listarPoblacionME'),
    path('administrarSVE/poblacionSVE/lista/correos', login_required(poblacionEnviarCorreo), name='enviarCorreosME'),
    path('administrarSVE/poblacionSVE/editar/<int:identificacion>', login_required(poblacionEdit), name='EditarPoblacionME'),
    path('administrarSVE/poblacionSVE/eliminar/<int:identificacion>', login_required(poblacionEliminar),name='EliminarPoblacionME'),


   
   






]
