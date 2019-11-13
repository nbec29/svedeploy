from django.urls import path
from apps.Riesgos.views import inicio, riesgoME, enfermedadME, administrarSVE, PoblacionCreate, \
    Poblacionlistar, poblacionEdit, poblacionEliminar, poblacionEnviarCorreo, EnviarMensaje, \
    notificaciones, aggEnfermedad, Enfermedad, aggDefEnfermedad, enfermedadMEEdit, enfermedadMEEliminar, \
    iniciarTestMEPiloto, informacionEnf, defEnfMEEdit, defEnfMEEliminar, aggRecomendaciones, listaRecomendaciones, \
    recomendacionesEdit, recomendacionesEliminar, estadisticas, estadistica1, estadistica2
from django.contrib.auth.decorators import login_required


urlpatterns = [
    path('', login_required(inicio), name='Inicio'),
    path('musculoEsqueletico', login_required(riesgoME), name='riesgoME'),
    
    path('musculoEsqueletico/testME/iniciarTestMEPiloto', login_required(iniciarTestMEPiloto), name='iniciarTestMEPiloto'),


    path('musculoEsqueletico/testME/enviado', login_required(EnviarMensaje), name='enfermedadesME'),
    path('administrarSVE', login_required(administrarSVE), name='administrarsve'),
    path('notificaciones', login_required(notificaciones), name='notificaciones'),
    path('administrarSVE/poblacionSVE', login_required(PoblacionCreate), name='poblacionSVE'),

    path('musculoEsqueletico/enfermedadesME', login_required(enfermedadME), name='enfermedadesME'),
    path('administrarSVE/enfermedades', login_required(Enfermedad), name='enfermedades'),
    path('administrarSVE/aggDefEnfermedades', login_required(aggDefEnfermedad), name='aggDefEnfermedades'),
    path('administrarSVE/aggenfermedad', login_required(aggEnfermedad), name='aggenfermedad'),
    path('administrarSVE/aggenfermedad/editar/<int:identificacion>', login_required(enfermedadMEEdit), name='enfermedadMEEdit'),
    path('administrarSVE/aggenfermedad/eliminar/<int:identificacion>', login_required(enfermedadMEEliminar),name='enfermedadMEEliminar'),
    path('administrarSVE/aggenfermedad/informacionEnf/<int:identificacion>', login_required(informacionEnf),name='informacionEnf'),
    path('administrarSVE/aggenfermedad/defEnfMEEliminar/<int:identificacion>', login_required(defEnfMEEliminar),name='defEnfMEEliminar'),
    path('administrarSVE/aggenfermedad/defEnfMEEdit/<int:identificacion>', login_required(defEnfMEEdit),name='defEnfMEEdit'),

    path('administrarSVE/aggRecomendaciones', login_required(aggRecomendaciones),name='aggRecomendaciones'),
    path('administrarSVE/listaRecomendaciones', login_required(listaRecomendaciones),name='listaRecomendaciones'),
    path('administrarSVE/recomendaciones/Editar/<int:identificacion>', login_required(recomendacionesEdit),name='recomendacionesEdit'),
    path('administrarSVE/recomendaciones/eliminar/<int:identificacion>', login_required(recomendacionesEliminar),name='recomendacionesEliminar'),


    path('administrarSVE/poblacionSVE/lista', login_required(Poblacionlistar), name='listarPoblacionME'),
    path('administrarSVE/poblacionSVE/lista/correos', login_required(poblacionEnviarCorreo), name='enviarCorreosME'),
    path('administrarSVE/poblacionSVE/editar/<int:identificacion>', login_required(poblacionEdit), name='EditarPoblacionME'),
    path('administrarSVE/poblacionSVE/eliminar/<int:identificacion>', login_required(poblacionEliminar),name='EliminarPoblacionME'),

    path('administrarSVE/estadisticas', login_required(estadisticas),name='estadisticas'),
    path('administrarSVE/estadistica1', login_required(estadistica1),name='estadistica1'),
    path('administrarSVE/estadistica2', login_required(estadistica2),name='estadistica2'),
   
   






]
