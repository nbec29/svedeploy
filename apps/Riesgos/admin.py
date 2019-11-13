from django.contrib import admin
from apps.Riesgos.models import Riesgo, PosibleEnfermedad, TestME, SabiasQue, poblacion, Cargo, Dependencia, \
    PerfilDemografico, HombroME, CuelloME, CodoME, ManoME, EspaldaBajaME, EspaldaDorsalME, DefinicionEnfermedad

# Register your models here.
admin.site.register(Riesgo)
admin.site.register(PosibleEnfermedad)
admin.site.register(TestME)
admin.site.register(SabiasQue)
admin.site.register(poblacion)
admin.site.register(Cargo)
admin.site.register(Dependencia)
admin.site.register(PerfilDemografico)
admin.site.register(HombroME)
admin.site.register(CuelloME)
admin.site.register(CodoME)
admin.site.register(ManoME)
admin.site.register(EspaldaBajaME)
admin.site.register(EspaldaDorsalME)
admin.site.register(DefinicionEnfermedad)
