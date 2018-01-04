from django.conf.urls import url, include
from django.contrib.auth.decorators import login_required
from .views import *
urlpatterns=[
	url(r'^$',index, name="inicio"),
	url(r'^aplicacion/inicio/$',login_required(app_index), name="app_inicio"),
	url(r'^aplicacion/inicio1/(?P<pk>[0-9]+)/$',home, name="app_inicio1"),
	url(r'^aplicacion/inicio2/(?P<pk>[0-9]+)/$',home, name="app_inicio2"),
    url(r'^aplicacion/materia/$',login_required(MateriaCreate.as_view()), name='materia'),
    url(r'^aplicacion/nota/(?P<pk>\d+)/$',login_required(post_new), name='nota'),
    url(r'^aplicacion/inscripciones/$',login_required(InscripcionCreate.as_view()), name='inscripcion'),
    url(r'^aplicacion/profesor/$',login_required(ProfesorCreate.as_view()), name='profesor'),
    url(r'^aplicacion/nivel/$',login_required(NivelCreate.as_view()), name='nivel'),
    url(r'^aplicacion/nivel1/$',login_required(nivel1_new), name='nivel1'),
    url(r'^aplicacion/nivel2/$',login_required(nivel2.as_view()), name='nivel2'),
    url(r'^aplicacion/nivel3/$',login_required(nivel3.as_view()), name='nivel3'),
    url(r'^aplicacion/confirmar/$',login_required(ConfirmarInscripcion), name='confirmar1'),

    url(r'^aplicacion/editar/(?P<pk>\d+)/$', login_required(SolicitudUpdate.as_view()), name='aplicacion_editar'),
    url(r'^aplicacion/eliminar/(?P<pk>\d+)/$', login_required(SolicitudDelete.as_view()), name='aplicacion_eliminar'),
    url(r'^aplicacion/listarpro/$',login_required(SolicitudListPro.as_view()), name='aplicacion_listarPro'),
    url(r'^aplicacion/listar_per/asdfv3sdd(?P<pk>[0-9]+)868asdfv31Ds7s213/$',login_required(buscar), name='listar_per'),

    url(r'^aplicacion/nueva/$',login_required(SolicitudCreate.as_view()), name='aplicacion_crear'),
	url(r'^aplicacion/pdf/$',login_required(ReportePersonasPDF.as_view()), name="reporte"),
    url(r'^aplicacion/ver_notas/$',login_required(notas_filter), name="ver_notas"),

]