from django.shortcuts import render
from apps.Riesgos.models import poblacion, PerfilDemografico, Riesgo, HombroME, CodoME, CuelloME, ManoME, \
    EspaldaDorsalME, EspaldaBajaME, Cargo, Dependencia, TestME, PosibleEnfermedad, DefinicionEnfermedad, SabiasQue
from apps.Riesgos.formularios import PoblacionForm, EnfermedadForm, DescripcionEnfermedadForm, \
    DescripcionRecomendacionesForm
from django.core.mail import send_mail
import random
from apps.Riesgos.redNeuronalME.Cargar_Modelo import predic
from django.urls import reverse
from django.http import HttpResponseRedirect
import csv
from django.db.models import Count



def normalizarDatos(entradas):
    print('pasa1')
    datos = entradas[0]
    print('pasa2')

    lugarMolestiaHombro = (datos[0] - 1) / (3 - 1)
    molestiaSepresentaHombro = (datos[1] - 1) / (4 - 1)
    laMolestiaEsHombro = (datos[2] - 1) / (5 - 1)
    seEfectuaMolestiaHombro = (datos[3] - 1) / (2 - 1)
    intensidadMolestiaHombro = (datos[4] - 1) / (10 - 1)
    otraActividadMolestaAuHombro = (datos[5] - 1) / (2 - 1)
    otraActividadMolestaDisHombro = (datos[6] - 1) / (2 - 1)
    duracionMolestiaHombro = (datos[7] - 1) / (4 - 1)
    interfirioTrabajoHombro = (datos[8] - 1) / (3 - 1)

    cuellolugarMolestia = (datos[9] - 1) / (3 - 1)
    cuellomolestiaSepresenta = (datos[10] - 1) / (4 - 1)
    cuellolaMolestiaEs = (datos[11] - 1) / (5 - 1)
    cuelloseEfectuaMolestia = (datos[12] - 1) / (4 - 1)
    cuellointensidadMolestia = (datos[13] - 1) / (10 - 1)
    cuellootraActividadMolestaAu = (datos[14] - 1) / (2 - 1)
    cuellootraActividadMolestaDis = (datos[15] - 1) / (2 - 1)
    cuelloduracionMolestia = (datos[16] - 1) / (4 - 1)
    cuellointerfirioTrabajo = (datos[17] - 1) / (3 - 1)

    codolugarMolestia = (datos[18] - 1) / (3 - 1)
    codomolestiaSepresenta = (datos[19] - 1) / (4 - 1)
    codolaMolestiaEs = (datos[20] - 1) / (5 - 1)
    codoseEfectuaMolestia = (datos[21] - 1) / (3 - 1)
    codointensidadMolestia = (datos[22] - 1) / (10 - 1)
    codootraActividadMolestaAu = (datos[23] - 1) / (2 - 1)
    codootraActividadMolestaDis = (datos[24] - 1) / (2 - 1)
    cododuracionMolestia = (datos[25] - 1) / (4 - 1)
    codointerfirioTrabajo = (datos[26] - 1) / (3 - 1)

    manolugarMolestia = (datos[27] - 1) / (3 - 1)
    manomolestiaSepresenta = (datos[28] - 1) / (4 - 1)
    manolaMolestiaEs = (datos[29] - 1) / (2 - 1)
    manoseEfectuaMolestia = (datos[30] - 1) / (3 - 1)
    manointensidadMolestia = (datos[31] - 1) / (10 - 1)
    manootraActividadMolestaAu = (datos[32] - 1) / (2 - 1)
    manootraActividadMolestaDis = (datos[33] - 1) / (2 - 1)
    manoduracionMolestia = (datos[34] - 1) / (4 - 1)
    manointerfirioTrabajo = (datos[35] - 1) / (3 - 1)

    espaldaDorsallugarMolestia = (datos[36] - 1) / (3 - 1)
    espaldaDorsalmolestiaSepresenta = (datos[37] - 1) / (4 - 1)
    espaldaDorsallaMolestiaEs = (datos[38] - 1) / (5 - 1)
    espaldaDorsaleEfectuaMolestia = (datos[39] - 1) / (3 - 1)
    espaldaDorsalintensidadMolestia = (datos[40] - 1) / (10 - 1)
    espaldaDorsalotraActividadMolestaAu = (datos[41] - 1) / (2 - 1)
    espaldaDorsalotraActividadMolestaDis = (datos[42] - 1) / (2 - 1)
    espaldaDorsalduracionMolestia = (datos[43] - 1) / (4 - 1)
    espaldaDorsalinterfirioTrabajo = (datos[44] - 1) / (3 - 1)

    espaldaBajalugarMolestia = (datos[45] - 1) / (3 - 1)
    espaldaBajamolestiaSepresenta = (datos[46] - 1) / (4 - 1)
    espaldaBajalaMolestiaEs = (datos[47] - 1) / (5 - 1)
    espaldaBajaeEfectuaMolestia = (datos[48] - 1) / (3 - 1)
    espaldaBajaintensidadMolestia = (datos[49] - 1) / (10 - 1)
    espaldaBajaotraActividadMolestaAu = (datos[50] - 1) / (2 - 1)
    espaldaBajaotraActividadMolestaDis = (datos[51] - 1) / (2 - 1)
    espaldaBajaduracionMolestia = (datos[52] - 1) / (4 - 1)
    espaldaBajainterfirioTrabajo = (datos[53] - 1) / (3 - 1)

    perfilDemograficoSexo = (datos[54] - 1) / (2 - 1)
    perfilDemograficoPeso = (datos[55] - 50) / (110 - 1)
    perfilDemograficoManoDomin = (datos[56] - 1) / (2 - 1)
    perfilDemograficoAntiguedadCargo = (datos[57] - 1) / (10 - 1)
    perfilDemograficoActividadFisica = (datos[58] - 1) / (2 - 1)
    perfilDemograficoHorasActividadFisi = (datos[59] - 1) / (4 - 1)
    perfilDemograficovariaSuJornada = (datos[60] - 1) / (2 - 1)
    perfilDemograficoCargo = (datos[61] - 1) / (30 - 1)
    perfilDemograficoDependencia = (datos[62] - 1) / (15 - 1)

    entradas1 = []
    entradas1.append(
        [
            'lugarMolestiaHombro',
            'molestiaSepresentaHombro',
            'laMolestiaEsHombro',
            'seEfectuaMolestiaHombro',
            'intensidadMolestiaHombro',
            'otraActividadMolestaAuHombro',
            'otraActividadMolestaDisHombro',
            'duracionMolestiaHombro',
            'interfirioTrabajoHombro',
            'cuellolugarMolestia',
            'cuellomolestiaSepresenta',
            'cuellolaMolestiaEs',
            'cuelloseEfectuaMolestia',
            'cuellointensidadMolestia',
            'cuellootraActividadMolestaAu',
            'cuellootraActividadMolestaDis',
            'cuelloduracionMolestia',
            'cuellointerfirioTrabajo',
            'codolugarMolestia',
            'codomolestiaSepresenta',
            'codolaMolestiaEs',
            'codoseEfectuaMolestia',
            'codointensidadMolestia',
            'codootraActividadMolestaAu',
            'codootraActividadMolestaDis',
            'cododuracionMolestia',
            'codointerfirioTrabajo',
            'manolugarMolestia',
            'manomolestiaSepresenta',
            'manolaMolestiaEs',
            'manoseEfectuaMolestia',
            'manointensidadMolestia',
            'manootraActividadMolestaAu',
            'manootraActividadMolestaDis',
            'manoduracionMolestia',
            'manointerfirioTrabajo',
            'espaldaDorsallugarMolestia',
            'espaldaDorsalmolestiaSepresenta',
            'espaldaDorsallaMolestiaEs',
            'espaldaDorsaleEfectuaMolestia',
            'espaldaDorsalintensidadMolestia',
            'espaldaDorsalotraActividadMolestaAu',
            'espaldaDorsalotraActividadMolestaDis',
            'espaldaDorsalduracionMolestia',
            'espaldaDorsalinterfirioTrabajo',
            'espaldaBajalugarMolestia',
            'espaldaBajamolestiaSepresenta',
            'espaldaBajalaMolestiaEs',
            'espaldaBajaeEfectuaMolestia',
            'espaldaBajaintensidadMolestia',
            'espaldaBajaotraActividadMolestaAu',
            'espaldaBajaotraActividadMolestaDis',
            'espaldaBajaduracionMolestia',
            'espaldaBajainterfirioTrabajo',
            'perfilDemograficoSexo',
            'perfilDemograficoPeso',
            'perfilDemograficoManoDomin',
            'perfilDemograficoAntiguedadCargo',
            'perfilDemograficoActividadFisica',
            'perfilDemograficoHorasActividadFisi',
            'perfilDemograficovariaSuJornada',
            'perfilDemograficoCargo',
            'perfilDemograficoDependencia',

        ]

    )

    entradas1.append(
        [
            float(lugarMolestiaHombro),
            float(molestiaSepresentaHombro),
            float(laMolestiaEsHombro),
            float(seEfectuaMolestiaHombro),
            float(intensidadMolestiaHombro),
            float(otraActividadMolestaAuHombro),
            float(otraActividadMolestaDisHombro),
            float(duracionMolestiaHombro),
            float(interfirioTrabajoHombro),

            float(cuellolugarMolestia),
            float(cuellomolestiaSepresenta),
            float(cuellolaMolestiaEs),
            float(cuelloseEfectuaMolestia),
            float(cuellointensidadMolestia),
            float(cuellootraActividadMolestaAu),
            float(cuellootraActividadMolestaDis),
            float(cuelloduracionMolestia),
            float(cuellointerfirioTrabajo),

            float(codolugarMolestia),
            float(codomolestiaSepresenta),
            float(codolaMolestiaEs),
            float(codoseEfectuaMolestia),
            float(codointensidadMolestia),
            float(codootraActividadMolestaAu),
            float(codootraActividadMolestaDis),
            float(cododuracionMolestia),
            float(codointerfirioTrabajo),

            float(manolugarMolestia),
            float(manomolestiaSepresenta),
            float(manolaMolestiaEs),
            float(manoseEfectuaMolestia),
            float(manointensidadMolestia),
            float(manootraActividadMolestaAu),
            float(manootraActividadMolestaDis),
            float(manoduracionMolestia),
            float(manointerfirioTrabajo),

            float(espaldaDorsallugarMolestia),
            float(espaldaDorsalmolestiaSepresenta),
            float(espaldaDorsallaMolestiaEs),
            float(espaldaDorsaleEfectuaMolestia),
            float(espaldaDorsalintensidadMolestia),
            float(espaldaDorsalotraActividadMolestaAu),
            float(espaldaDorsalotraActividadMolestaDis),
            float(espaldaDorsalduracionMolestia),
            float(espaldaDorsalinterfirioTrabajo),

            float(espaldaBajalugarMolestia),
            float(espaldaBajamolestiaSepresenta),
            float(espaldaBajalaMolestiaEs),
            float(espaldaBajaeEfectuaMolestia),
            float(espaldaBajaintensidadMolestia),
            float(espaldaBajaotraActividadMolestaAu),
            float(espaldaBajaotraActividadMolestaDis),
            float(espaldaBajaduracionMolestia),
            float(espaldaBajainterfirioTrabajo),
            float(perfilDemograficoSexo),
            float(perfilDemograficoPeso),
            float(perfilDemograficoManoDomin),
            float(perfilDemograficoAntiguedadCargo),
            float(perfilDemograficoActividadFisica),
            float(perfilDemograficoHorasActividadFisi),
            float(perfilDemograficovariaSuJornada),
            float(perfilDemograficoCargo),
            float(perfilDemograficoDependencia),

        ]

    )

    archivo = open('Eprediccion.csv', 'w')

    with archivo:
        writer = csv.writer(archivo, delimiter=',')
        writer.writerows(entradas1)

    return True


def filtroSabiasQue():
    sabiasQue = SabiasQue.objects.all()
    cantidad = 0
    for sabias in sabiasQue:
        cantidad += 1
    cantidad -= 1
    cantidad = (random.randrange(cantidad))

    sabiasQue = sabiasQue[cantidad]
    return sabiasQue


# Create your views here.
def inicio(request):
    sabiasQue = filtroSabiasQue
    return render(request, 'SVE/homepage.html', {'sabiasQues': sabiasQue})


def riesgoME(request):
    sabiasQue = filtroSabiasQue
    return render(request, 'RiesgoME/musculoEsqueletico.html', {'sabiasQues': sabiasQue})


def administrarSVE(request):
    sabiasQue = filtroSabiasQue
    return render(request, 'SVE/administrarSVE.html', {'sabiasQues': sabiasQue})


def EnviarMensaje(request):
    sabiasQue = filtroSabiasQue

    return render(request, 'RiesgoME/mensajeME.html', {'sabiasQues': sabiasQue})


def PoblacionCreate(request):
    sabiasQue = filtroSabiasQue
    if request.method == 'POST':
        form = PoblacionForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = PoblacionForm()
    return render(request, 'SVE/poblacionSVE.html', {'form': form, 'sabiasQues': sabiasQue})


def Poblacionlistar(request):
    sabiasQue = filtroSabiasQue
    Poblacion = poblacion.objects.filter(Riesgo=1)
    contexto = {'poblaciones': Poblacion, 'sabiasQues': sabiasQue}
    return render(request, 'RiesgoME/listaPoblacion.html', contexto)


def poblacionEdit(request, identificacion):
    sabiasQue = filtroSabiasQue
    Poblacion = poblacion.objects.get(identificacion=identificacion)
    if request.method == 'GET':
        form = PoblacionForm(instance=Poblacion)
    else:
        form = PoblacionForm(request.POST, instance=Poblacion)
        if form.is_valid():
            form.save()
    return render(request, 'SVE/poblacionSVE.html', {'form': form, 'sabiasQues': sabiasQue})


def poblacionEliminar(request, identificacion):
    sabiasQue = filtroSabiasQue
    Poblacion = poblacion.objects.get(identificacion=identificacion)
    if request.method == 'POST':
        Poblacion.delete()
    return render(request, 'RiesgoME/eliminarPoblacionME.html', {'poblacion': Poblacion, 'sabiasQues': sabiasQue})


def poblacionEnviarCorreo(request):
    sabiasQue = filtroSabiasQue
    Poblacion = poblacion.objects.filter(Riesgo=1)
    correo = []
    for correos in Poblacion:
        correo.append(correos.correo)
    subject = 'Hola soy in correo de prueba'
    message = ' Correo de prueba SVE '
    email_from = 'jbarrera1235@gmail.com'
    recipient_list = correo
    send_mail(subject, message, email_from, recipient_list)
    return render(request, 'RiesgoME/enviarCorreoME.html', {'sabiasQues': sabiasQue})


def notificaciones(request):
    sabiasQue = filtroSabiasQue
    perfilDemografico = PerfilDemografico.objects.all()
    contexto = {'perfilDemograficos': perfilDemografico, 'sabiasQues': sabiasQue}

    return render(request, 'SVE/notificaciones.html', contexto)


def iniciarTestMEPiloto(request):
    sabiasQue = filtroSabiasQue
    if request.method == 'POST':
        test2 = None

        lugarMolestiaHombro = 0
        if request.POST.get('ladoDolor') is not None:
            lugarMolestiaHombro = request.POST.get('ladoDolor')

        molestiaSepresentaHombro = request.POST.get('Generalmente se presentan como:')
        laMolestiaEsHombro = request.POST.get('Seleccione cada cuanto presenta la sintomatologia en su hombro')
        seEfectuaMolestiaHombro = request.POST.get('La molestia se presenta cuando efectua que tipo de movimientos:')
        intensidadMolestiaHombro = request.POST.get('IntensidadHombro')

        otraActividadMolestaAuHombro = 0
        if request.POST.get('actividadAumHombro') is not None:
            otraActividadMolestaAuHombro = request.POST.get('actividadAumHombro')

        otraActividadMolestaDisHombro = 0
        if request.POST.get('actividadDismHombro') is not None:
            otraActividadMolestaDisHombro = request.POST.get('actividadDismHombro')

        duracionMolestiaHombro = request.POST.get('Cuanto dura aproximadamente cada episodio de molestia o dolor')
        interfirioTrabajoHombro = request.POST.get('Cuánto interfirió con su habilidad para trabajar')

        print(lugarMolestiaHombro, "   LUGAR MOLESTIA")
        print(laMolestiaEsHombro, "   Seleccione cada cuanto presenta la sintomatologia en su hombro")
        print(molestiaSepresentaHombro, "   Generalmente se presentan como:")
        print(seEfectuaMolestiaHombro, "   La molestia se presenta cuando efectua que tipo de movimientos:")
        print(intensidadMolestiaHombro, "   IntensidadHombro")
        print(otraActividadMolestaAuHombro, "   actividadAumHombro")
        print(otraActividadMolestaDisHombro, "   actividadDismHombro")
        print(duracionMolestiaHombro, "   Cuanto dura aproximadamente cada episodio de molestia o dolor")
        print(interfirioTrabajoHombro, "   Cuánto interfirió con su habilidad para trabajar")

        cuellolugarMolestia = 0
        if request.POST.get('ladoDolorCuello') is not None:
            cuellolugarMolestia = request.POST.get('ladoDolorCuello')

        cuellomolestiaSepresenta = request.POST.get('Generalmente se presentan como: Cuello')
        cuellolaMolestiaEs = request.POST.get('Seleccione cada cuanto presenta la sintomatologia en su Cuello')
        cuelloseEfectuaMolestia = request.POST.get(
            'La molestia se presenta cuando efectua que tipo de movimientos: Cuello')
        cuellointensidadMolestia = request.POST.get('IntensidadCuello')
        cuellootraActividadMolestaAu = 0
        if request.POST.get('actividadAumCuello') is not None:
            cuellootraActividadMolestaAu = request.POST.get('actividadAumCuello')

        cuellootraActividadMolestaDis = 0
        if request.POST.get('actividadDismCuello') is not None:
            cuellootraActividadMolestaDis = request.POST.get('actividadDismCuello')
        cuelloduracionMolestia = request.POST.get(
            'Cuanto dura aproximadamente cada episodio de molestia o dolor : Cuello')
        cuellointerfirioTrabajo = request.POST.get('Cuánto interfirió con su habilidad para trabajar : Cuello')

        print("SECCIÓN CUELLO")
        print(cuellolugarMolestia, "   LUGAR MOLESTIA")
        print(cuellolaMolestiaEs, "   Seleccione cada cuanto presenta la sintomatologia en su CUELLO")
        print(cuellomolestiaSepresenta, "   Generalmente se presentan como:")
        print(cuelloseEfectuaMolestia, "   La molestia se presenta cuando efectua que tipo de movimientos:")
        print(cuellointensidadMolestia, "   IntensidadCUELLO")
        print(cuellootraActividadMolestaAu, "   actividadAumCUELLO")
        print(cuellootraActividadMolestaDis, "   actividadDismCUELLO")
        print(cuelloduracionMolestia, "   Cuanto dura aproximadamente cada episodio de molestia o dolor")
        print(cuellointerfirioTrabajo, "   Cuánto interfirió con su habilidad para trabajar : Cuello")

        codolugarMolestia = 0
        if request.POST.get('ladoDolorCodo') is not None:
            codolugarMolestia = request.POST.get('ladoDolorCodo')

        codomolestiaSepresenta = request.POST.get('Generalmente se presentan como: Codo')
        codolaMolestiaEs = request.POST.get('Seleccione cada cuanto presenta la sintomatologia en su Codo')
        codoseEfectuaMolestia = request.POST.get('La molestia se presenta cuando efectua que tipo de movimientos: Codo')
        codointensidadMolestia = request.POST.get('IntensidadCodo')

        codootraActividadMolestaAu = 0
        if request.POST.get('actividadAumCodo') is not None:
            codootraActividadMolestaAu = request.POST.get('actividadAumCodo')

        codootraActividadMolestaDis = 0
        if request.POST.get('actividadDismCodo') is not None:
            codootraActividadMolestaDis = request.POST.get('actividadDismCodo')

        cododuracionMolestia = request.POST.get('Cuanto dura aproximadamente cada episodio de molestia o dolor : Codo')
        codointerfirioTrabajo = request.POST.get('Cuánto interfirió con su habilidad para trabajar : Codo')

        print("SECCIÓN CODO")
        print(codolugarMolestia, "   LUGAR MOLESTIA")
        print(codomolestiaSepresenta, "   Seleccione cada cuanto presenta la sintomatologia en su CODO")
        print(codolaMolestiaEs, "   Generalmente se presentan como:")
        print(codoseEfectuaMolestia, "   La molestia se presenta cuando efectua que tipo de movimientos:")
        print(codointensidadMolestia, "   IntensidadCODO")
        print(codootraActividadMolestaAu, "   actividadAumCODO")
        print(cuellootraActividadMolestaDis, "   actividadDismCUELLO")
        print(codootraActividadMolestaDis, "   Cuanto dura aproximadamente cada episodio de molestia o dolor")
        print(codointerfirioTrabajo, "   Cuánto interfirió con su habilidad para trabajar")

        manolugarMolestia = 0
        if request.POST.get('ladoDolorMano') is not None:
            manolugarMolestia = request.POST.get('ladoDolorMano')

        manomolestiaSepresenta = request.POST.get('Generalmente se presentan como: Mano')
        manolaMolestiaEs = request.POST.get('Seleccione cada cuanto presenta la sintomatologia en su Mano')
        manoseEfectuaMolestia = request.POST.get('La molestia se presenta cuando efectua que tipo de movimientos: Mano')
        manointensidadMolestia = request.POST.get('IntensidadMano')

        manootraActividadMolestaAu = 0
        if request.POST.get('actividadAumMano') is not None:
            manootraActividadMolestaAu = request.POST.get('actividadAumMano')

        manootraActividadMolestaDis = 0
        if request.POST.get('actividadDismCodo') is not None:
            manootraActividadMolestaDis = request.POST.get('actividadDismCodo')

        manoduracionMolestia = request.POST.get('Cuanto dura aproximadamente cada episodio de molestia o dolor : Mano')
        manointerfirioTrabajo = request.POST.get('Cuánto interfirió con su habilidad para trabajar : Mano')

        espaldaDorsallugarMolestia = 0
        if request.POST.get('ladoDolorespaldaDorsal') is not None:
            espaldaDorsallugarMolestia = request.POST.get('ladoDolorespaldaDorsal')

        espaldaDorsalmolestiaSepresenta = request.POST.get('Generalmente se presentan como: espalda Dorsal')
        espaldaDorsallaMolestiaEs = request.POST.get(
            'Seleccione cada cuanto presenta la sintomatologia en su espalda Dorsal')
        espaldaDorsaleEfectuaMolestia = request.POST.get(
            'La molestia se presenta cuando efectua que tipo de movimientos: espalda Dorsal')
        espaldaDorsalintensidadMolestia = request.POST.get('IntensidadespaldaDorsal')

        espaldaDorsalotraActividadMolestaAu = 0
        if request.POST.get('actividadAumespaldaDorsal') is not None:
            espaldaDorsalotraActividadMolestaAu = request.POST.get('actividadAumespaldaDorsal')

        espaldaDorsalotraActividadMolestaDis = 0
        if request.POST.get('actividadAumespaldaDorsal') is not None:
            espaldaDorsalotraActividadMolestaDis = request.POST.get('actividadDismespaldaDorsal')

        espaldaDorsalduracionMolestia = request.POST.get(
            'Cuanto dura aproximadamente cada episodio de molestia o dolor : espalda Dorsal')
        espaldaDorsalinterfirioTrabajo = request.POST.get(
            'Cuánto interfirió con su habilidad para trabajar : espalda Dorsal')

        espaldaBajalugarMolestia = 0
        if request.POST.get('actividadAumespaldaDorsal') is not None:
            espaldaBajalugarMolestia = request.POST.get('ladoDolorespaldaBaja')

        espaldaBajamolestiaSepresenta = request.POST.get('Generalmente se presentan como: espalda Baja')
        espaldaBajalaMolestiaEs = request.POST.get(
            'Seleccione cada cuanto presenta la sintomatologia en su espalda Baja')
        espaldaBajaeEfectuaMolestia = request.POST.get(
            'La molestia se presenta cuando efectua que tipo de movimientos: espalda Baja')
        espaldaBajaintensidadMolestia = request.POST.get('IntensidadespaldaBaja')

        espaldaBajaotraActividadMolestaAu = 0
        if request.POST.get('actividadAumespaldaDorsal') is not None:
            espaldaBajaotraActividadMolestaAu = request.POST.get('actividadAumespaldaBaja')

        espaldaBajaotraActividadMolestaDis = 0
        if request.POST.get('actividadDismespaldaBaja') is not None:
            espaldaBajaotraActividadMolestaDis = request.POST.get('actividadDismespaldaBaja')

        espaldaBajaduracionMolestia = request.POST.get(
            'Cuanto dura aproximadamente cada episodio de molestia o dolor : espalda Baja')
        espaldaBajainterfirioTrabajo = request.POST.get(
            'Cuánto interfirió con su habilidad para trabajar : espalda Baja')

        print("SECCIÓN ESPALDA BAJA")
        print(espaldaBajalugarMolestia, "   LUGAR MOLESTIA")
        print(espaldaBajamolestiaSepresenta, "   Generalmente se presentan como: espalda Baja")
        print(espaldaBajalaMolestiaEs, "   Seleccione cada cuanto presenta la sintomatologia en su espalda Baja")
        print(codoseEfectuaMolestia, "   La molestia se presenta cuando efectua que tipo de movimientos:")
        print(codointensidadMolestia, "   IntensidadCODO")
        print(codootraActividadMolestaAu, "   actividadAumCODO")
        print(cuellootraActividadMolestaDis, "   actividadDismCUELLO")
        print(codootraActividadMolestaDis, "   Cuanto dura aproximadamente cada episodio de molestia o dolor")
        print(codointerfirioTrabajo, "   Cuánto interfirió con su habilidad para trabajar")

        perfilDemograficoSexo = request.POST.get('generoUsuarioEs')

        print(perfilDemograficoSexo, "   GENEROOOOOOOOOOOOOOOOOOOOOOOOOOOO")

        perfilDemograficoPeso = request.POST.get('peso')
        perfilDemograficoManoDomin = request.POST.get('mano')
        aniosCargo = float(request.POST.get('anios'))
        mesesCargo = float(request.POST.get('meses')) / 12
        if (aniosCargo == 0 or aniosCargo is None):
            aniosCargo = 0
        elif (mesesCargo == 0 or mesesCargo is None):
            mesesCargo = 0
        perfilDemograficoAntiguedadCargo = aniosCargo + mesesCargo
        perfilDemograficoActividadFisica = request.POST.get('actividad')
        perfilDemograficoHorasActividadFisi = request.POST.get('trabajoDiario')
        perfilDemograficovariaSuJornada = request.POST.get('semanal')
        perfilDemograficoCargo = request.POST.get('Cargo actual')
        perfilDemograficoDependencia = request.POST.get('Seleccione su Dependencia')
        perfilDemograficoNombre = request.POST.get('nombre')
        perfilDemograficoApellido = request.POST.get('apellido')
        perfilDemograficoCedula = request.POST.get('cedula')

        print("SECCIÓN SOCIO DEMOGRAFICO")
        print(perfilDemograficoSexo, "   GENEROOOOOOOOOOOOOOOOOOOOOOOOOOOO")
        print(perfilDemograficoPeso, "   PESO")
        print(perfilDemograficoManoDomin, "   MANO")
        print(perfilDemograficoAntiguedadCargo, "   ANTIGUEDAD CARGO")
        print(perfilDemograficoActividadFisica, "   ACTIVIDAD FISICA")
        print(perfilDemograficoHorasActividadFisi, "   TRABAJO DIARIO")
        print(perfilDemograficovariaSuJornada, "   VARIA SEMANALMENTE")
        print(perfilDemograficoCargo, "   CARGO ACTUAL")
        print(perfilDemograficoDependencia, "   DEPENDENCIA")
        entradas = []
        entradas.append(
            [
                float(lugarMolestiaHombro),
                float(molestiaSepresentaHombro),
                float(laMolestiaEsHombro),
                float(seEfectuaMolestiaHombro),
                float(intensidadMolestiaHombro),
                float(otraActividadMolestaAuHombro),
                float(otraActividadMolestaDisHombro),
                float(duracionMolestiaHombro),
                float(interfirioTrabajoHombro),
                float(cuellolugarMolestia),
                float(cuellomolestiaSepresenta),
                float(cuellolaMolestiaEs),
                float(cuelloseEfectuaMolestia),
                float(cuellointensidadMolestia),
                float(cuellootraActividadMolestaAu),
                float(cuellootraActividadMolestaDis),
                float(cuelloduracionMolestia),
                float(cuellointerfirioTrabajo),
                float(codolugarMolestia),
                float(codomolestiaSepresenta),
                float(codolaMolestiaEs),
                float(codoseEfectuaMolestia),
                float(codointensidadMolestia),
                float(codootraActividadMolestaAu),
                float(codootraActividadMolestaDis),
                float(cododuracionMolestia),
                float(codointerfirioTrabajo),
                float(manolugarMolestia),
                float(manomolestiaSepresenta),
                float(manolaMolestiaEs),
                float(manoseEfectuaMolestia),
                float(manointensidadMolestia),
                float(manootraActividadMolestaAu),
                float(manootraActividadMolestaDis),
                float(manoduracionMolestia),
                float(manointerfirioTrabajo),
                float(espaldaDorsallugarMolestia),
                float(espaldaDorsalmolestiaSepresenta),
                float(espaldaDorsallaMolestiaEs),
                float(espaldaDorsaleEfectuaMolestia),
                float(espaldaDorsalintensidadMolestia),
                float(espaldaDorsalotraActividadMolestaAu),
                float(espaldaDorsalotraActividadMolestaDis),
                float(espaldaDorsalduracionMolestia),
                float(espaldaDorsalinterfirioTrabajo),
                float(espaldaBajalugarMolestia),
                float(espaldaBajamolestiaSepresenta),
                float(espaldaBajalaMolestiaEs),
                float(espaldaBajaeEfectuaMolestia),
                float(espaldaBajaintensidadMolestia),
                float(espaldaBajaotraActividadMolestaAu),
                float(espaldaBajaotraActividadMolestaDis),
                float(espaldaBajaduracionMolestia),
                float(espaldaBajainterfirioTrabajo),
                float(perfilDemograficoSexo),
                float(perfilDemograficoPeso),
                float(perfilDemograficoManoDomin),
                float(perfilDemograficoAntiguedadCargo),
                float(perfilDemograficoActividadFisica),
                float(perfilDemograficoHorasActividadFisi),
                float(perfilDemograficovariaSuJornada),
                float(perfilDemograficoCargo),
                float(perfilDemograficoDependencia),

            ]

        )

        entradasNormal = normalizarDatos(entradas)
        if (entradasNormal == True):

            riesgo = Riesgo.objects.filter(id=1).get()
            test = TestME(idRiesgo=riesgo, usuario=request.user)
            test.save()

            hombro = HombroME(test1=test,
                              lugarMolestia1=lugarMolestiaHombro,
                              molestiaSepresenta1=molestiaSepresentaHombro,
                              laMolestiaEs1=laMolestiaEsHombro,
                              seEfectuaMolestia1=seEfectuaMolestiaHombro,
                              intensidadMolestia1=intensidadMolestiaHombro,
                              otraActividadMolestaAu1=otraActividadMolestaAuHombro,
                              otraActividadMolestaDis1=otraActividadMolestaDisHombro,
                              duracionMolestia1=duracionMolestiaHombro,
                              interfirioTrabajo1=interfirioTrabajoHombro)
            hombro.save()

            cuello = CuelloME(test2=test,
                              lugarMolestia2=cuellolugarMolestia,
                              molestiaSepresenta2=cuellomolestiaSepresenta,
                              laMolestiaEs2=cuellolaMolestiaEs,
                              seEfectuaMolestia2=cuelloseEfectuaMolestia,
                              intensidadMolestia2=cuellointensidadMolestia,
                              otraActividadMolestaAu2=cuellootraActividadMolestaAu,
                              otraActividadMolestaDis2=cuellootraActividadMolestaDis,
                              duracionMolestia2=cuelloduracionMolestia,
                              interfirioTrabajo2=cuellointerfirioTrabajo)

            cuello.save()

            codo = CodoME(test3=test,
                          lugarMolestia3=codolugarMolestia,
                          molestiaSepresenta3=codomolestiaSepresenta,
                          laMolestiaEs3=codolaMolestiaEs,
                          seEfectuaMolestia3=codoseEfectuaMolestia,
                          intensidadMolestia3=codointensidadMolestia,
                          otraActividadMolestaAu3=codootraActividadMolestaAu,
                          otraActividadMolestaDis3=codootraActividadMolestaDis,
                          duracionMolestia3=cododuracionMolestia,
                          interfirioTrabajo3=codointerfirioTrabajo)

            codo.save()

            mano = ManoME(test4=test,
                          lugarMolestia4=manolugarMolestia,
                          molestiaSepresenta4=manomolestiaSepresenta,
                          laMolestiaEs4=manolaMolestiaEs,
                          seEfectuaMolestia4=manoseEfectuaMolestia,
                          intensidadMolestia4=manointensidadMolestia,
                          otraActividadMolestaAu4=manootraActividadMolestaAu,
                          otraActividadMolestaDis4=manootraActividadMolestaDis,
                          duracionMolestia4=manoduracionMolestia,
                          interfirioTrabajo4=manointerfirioTrabajo)
            mano.save()

            espaldaBaja = EspaldaBajaME(test5=test,
                                        lugarMolestia5=espaldaBajalugarMolestia,
                                        molestiaSepresenta5=espaldaBajamolestiaSepresenta,
                                        laMolestiaEs5=espaldaBajalaMolestiaEs,
                                        seEfectuaMolestia5=espaldaBajaeEfectuaMolestia,
                                        intensidadMolestia5=espaldaBajaintensidadMolestia,
                                        otraActividadMolestaAu5=espaldaBajaotraActividadMolestaAu,
                                        otraActividadMolestaDis5=espaldaBajaotraActividadMolestaDis,
                                        duracionMolestia5=espaldaBajaduracionMolestia,
                                        interfirioTrabajo5=espaldaBajainterfirioTrabajo)
            espaldaBaja.save()

            espaldaDorsal = EspaldaDorsalME(test6=test,
                                            lugarMolestia6=espaldaDorsallugarMolestia,
                                            molestiaSepresenta6=espaldaDorsalmolestiaSepresenta,
                                            laMolestiaEs6=espaldaDorsallaMolestiaEs,
                                            seEfectuaMolestia6=espaldaDorsaleEfectuaMolestia,
                                            intensidadMolestia6=espaldaDorsalintensidadMolestia,
                                            otraActividadMolestaAu6=espaldaDorsalotraActividadMolestaAu,
                                            otraActividadMolestaDis6=espaldaDorsalotraActividadMolestaDis,
                                            duracionMolestia6=espaldaDorsalduracionMolestia,
                                            interfirioTrabajo6=espaldaDorsalinterfirioTrabajo)

            espaldaDorsal.save()

            if perfilDemograficoSexo == '1':
                perfilDemograficoSexo = True
            else:
                perfilDemograficoSexo = False

            print(perfilDemograficoCedula, "CEDULAAAAAAAAAAAAAAAAAA")
            print(perfilDemograficoSexo, "GENEROOOOOOOOOOOOOOOOO ")
            cargo = Cargo.objects.filter(id=perfilDemograficoCargo).get()
            dependencia = Dependencia.objects.filter(id=perfilDemograficoDependencia).get()
            perfilDemografico = PerfilDemografico(test0=test,
                                                  cedula0=perfilDemograficoCedula,
                                                  nombre0=perfilDemograficoNombre,
                                                  apellido0=perfilDemograficoApellido,
                                                  sexo0=True,
                                                  peso0=float(perfilDemograficoPeso),
                                                  manoDominante0=perfilDemograficoManoDomin,
                                                  cargo0=cargo,
                                                  dependencia0=dependencia,
                                                  antiguedadCargo0=float(perfilDemograficoAntiguedadCargo),
                                                  actividadFisica0=perfilDemograficoActividadFisica,
                                                  horasActividadFisi0=int(perfilDemograficoHorasActividadFisi),
                                                  variaSuJornada0=True)
            perfilDemografico.save()
            prediccion = predic()
            prediccion = prediccion.predecir()
            print(prediccion)

            idtest = test.id

            test1 = TestME.objects.filter(id=idtest).update(diagnostico=prediccion)
            test2 = TestME.objects.filter(id=idtest)

    return render(request, 'hombro.html', {'sabiasQues': sabiasQue})


def enviarCorreoDiagnostico(prediccion, perfilDemografico, user):
    correo = []
    for correos in correo:
        correo.append('jbarrera12345@gmail.com')
    datos = 'predicción', prediccion, 'cedula', perfilDemografico.cedula0, 'cargo', perfilDemografico.cargo0.nombre, 'dpendencia', perfilDemografico.dependencia0.nombre

    subject = 'Diagnostico de Riesgo Musculo-Esqueletico'
    message = datos
    list_email = correo
    email_from = 'jbarrera1235@gmail.com'
    send_mail(subject, message, email_from, list_email)


def aggEnfermedad(request):
    sabiasQue = filtroSabiasQue
    if request.method == 'POST':
        form = EnfermedadForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = EnfermedadForm()
    return render(request, 'SVE/aggEnfermedad.html', {'form': form, 'sabiasQues': sabiasQue})

    return render(request, 'SVE/aggDescripcionEnfer.html', {'enfermedades': enfermedad})


def aggDefEnfermedad(request):
    sabiasQue = filtroSabiasQue
    if request.method == 'POST':
        form = DescripcionEnfermedadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    else:
        form = DescripcionEnfermedadForm()
    return render(request, 'SVE/aggDescripcionEnfer.html', {'form': form, 'sabiasQues': sabiasQue})


def Enfermedad(request):
    sabiasQue = filtroSabiasQue

    return render(request, 'SVE/enfermedades.html', {'sabiasQues': sabiasQue})


def enfermedadME(request):
    sabiasQue = filtroSabiasQue
    posibleEnfermedad = PosibleEnfermedad.objects.filter(idRiesgo=1)
    contexto = {'posibleEnfermedades': posibleEnfermedad, 'sabiasQues': sabiasQue}

    return render(request, 'RiesgoME/enfermedadesME.html', contexto)


def enfermedadMEEdit(request, identificacion):
    sabiasQue = filtroSabiasQue
    posibleEnfermedad = PosibleEnfermedad.objects.get(id=identificacion)
    if request.method == 'GET':
        form = EnfermedadForm(instance=posibleEnfermedad)
    else:
        form = EnfermedadForm(request.POST, instance=posibleEnfermedad)
        if form.is_valid():
            form.save()
    return render(request, 'SVE/aggEnfermedad.html', {'form': form, 'sabiasQues': sabiasQue})


def enfermedadMEEliminar(request, identificacion):
    sabiasQue = filtroSabiasQue
    posibleEnfermedad = PosibleEnfermedad.objects.get(id=identificacion)
    if request.method == 'POST':
        posibleEnfermedad.delete()
    return render(request, 'RiesgoME/eliminarEnfermedadME.html',
                  {'posibleEnfermedad': posibleEnfermedad, 'sabiasQues': sabiasQue})


def informacionEnf(request, identificacion):
    sabiasQue = filtroSabiasQue
    definicionEnfermedad = DefinicionEnfermedad.objects.filter(enfermedad=identificacion)
    contexto = {'definicionEnfermedades': definicionEnfermedad, 'sabiasQues': sabiasQue}
    return render(request, 'RiesgoME/informacionEnf.html', contexto)


def defEnfMEEdit(request, identificacion):
    sabiasQue = filtroSabiasQue
    definicionEnfermedad = DefinicionEnfermedad.objects.get(id=identificacion)
    if request.method == 'GET':
        form = DescripcionEnfermedadForm(instance=definicionEnfermedad)
    else:
        form = DescripcionEnfermedadForm(request.POST, request.FILES, instance=definicionEnfermedad)
        if form.is_valid():
            form.save()
    return render(request, 'SVE/aggDescripcionEnfer.html', {'form': form, 'sabiasQues': sabiasQue})


def defEnfMEEliminar(request, identificacion):
    sabiasQue = filtroSabiasQue
    print('entro')
    definicionEnfermedad = DefinicionEnfermedad.objects.get(id=identificacion)

    if request.method == 'POST':
        idEnfermedad = str(definicionEnfermedad.enfermedad.id)
        print(idEnfermedad)
        definicionEnfermedad.delete()
        return HttpResponseRedirect(reverse('informacionEnf', args=(idEnfermedad)))
    return render(request, 'RiesgoME/eliminarDefEnfer.html',
                  {'definicionEnfermedad': definicionEnfermedad, 'sabiasQues': sabiasQue})


def aggRecomendaciones(request):
    sabiasQue = filtroSabiasQue
    if request.method == 'POST':
        form = DescripcionRecomendacionesForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    else:
        form = DescripcionRecomendacionesForm()
    return render(request, 'SVE/crearRecomendaciones.html', {'form': form, 'sabiasQues': sabiasQue})


def listaRecomendaciones(request):
    sabiasQue = SabiasQue.objects.all()
    contexto = {'sabiasQues': sabiasQue}

    return render(request, 'SVE/listaRecomendaciones.html', contexto)


def recomendacionesEdit(request, identificacion):
    sabiasQue = SabiasQue.objects.get(id=identificacion)
    if request.method == 'GET':
        form = DescripcionRecomendacionesForm(instance=sabiasQue)
    else:
        form = DescripcionRecomendacionesForm(request.POST, request.FILES, instance=sabiasQue)
        if form.is_valid():
            form.save()
    return render(request, 'SVE/crearRecomendaciones.html', {'form': form})


def recomendacionesEliminar(request, identificacion):
    sabiasQue = SabiasQue.objects.get(id=identificacion)

    if request.method == 'POST':
        sabiasQue.delete()
        return HttpResponseRedirect(reverse('listaRecomendaciones'))
    return render(request, 'RiesgoME/eliminarDefEnfer.html', {'sabiasQue': sabiasQue})


def estadisticas(request):
    return render(request, 'SVE/estadisticas.html')


def estadistica1(request):
    data = dict
    data = PerfilDemografico.objects.values_list('cargo0__nombre').annotate(dcount=Count('cargo0'))

    return render(request, 'SVE/estadistica1.html', {'datas': data})


def estadistica2(request):
    data = dict
    data = PerfilDemografico.objects.values_list('dependencia0__nombre').annotate(dcount=Count('dependencia0'))

    return render(request, 'SVE/estadistica2.html', {'datas': data})
