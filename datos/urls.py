from django.conf.urls import url, include
from django.contrib.auth.decorators import login_required
from .views import *
urlpatterns=[
	url(r'^$',index, name="inicio"),
    url(r'^password/$', login_required(change_password), name='change_password'),
	url(r'^aplicacion/inicio/$',login_required(app_index), name="app_inicio"),
    url(r'^aplicacion/materia/$',login_required(MateriaCreate.as_view()), name='materia'),
    url(r'^aplicacion/nota/(?P<pk>[0-9]+)/$',login_required(post_new), name='nota'),
    url(r'^aplicacion/inscripciones/$',login_required(InscripcionCreate.as_view()), name='inscripcion'),
    url(r'^aplicacion/profesor/$',login_required(ProfesorCreate), name='profesor'),
    url(r'^aplicacion/nivel/$',login_required(NivelCreate.as_view()), name='nivel'),
    url(r'^aplicacion/nivel_ver/$',login_required(nivel1_new), name='nivel1'),

    url(r'^aplicacion/editar/(?P<pk>\d+)/$', login_required(SolicitudUpdate.as_view()), name='aplicacion_editar'),
    url(r'^aplicacion/eliminar/(?P<pk>\d+)/$', login_required(SolicitudDelete.as_view()), name='aplicacion_eliminar'),
    url(r'^aplicacion/listarpro/$',login_required(SolicitudListPro.as_view()), name='aplicacion_listarPro'),
    url(r'^aplicacion/listar_per/(?P<pk>[0-9]+)/$',login_required(buscar), name='listar_per'),

    url(r'^aplicacion/nueva/$',login_required(SolicitudCreate.as_view()), name='aplicacion_crear'),
	url(r'^aplicacion/pdf/$',login_required(generar_pdf.as_view()), name="reporte"),
    url(r'^aplicacion/pdf_personal/(?P<pk>\d+)/$',login_required(generar_pdf_personal.as_view()), name="reporte_personal"),
    url(r'^aplicacion/crear_usuario_profesor/$',UsersCreateView_profesor, name="crear_usuario_profesor"),
    url(r'^aplicacion/asignar_materias/$',login_required(AsignarMateria), name="asigna"),

    url(r'^aplicacion/ver_notas/$',login_required(notas_filter), name="ver_notas"),
    url(r'^notificaciones/(?P<pk>\d+)/$',login_required(notificacion), name="notificacion"),
    url(r'^aplicacion/ver_profesores/$',login_required(ListProfesor.as_view()), name="ver_profesores"),
    url(r'^aplicacion/ver_asignaciones/$',login_required(ListAsignarMateria.as_view()), name="ver_asignaciones"),
    url(r'^aplicacion/solicitud/$',login_required(solicitud), name="solicitud"),

    url(r'^aplicacion/nivel1/$',login_required(nivel1_superuser), name="nivel_1"),
    url(r'^aplicacion/nivel2/$',login_required(nivel2_superuser), name="nivel_2"),
    url(r'^aplicacion/nivel3/$',login_required(nivel3_superuser), name="nivel_3"),
    url(r'^aplicacion/ver_notas_super/(?P<pk>\d+)/$',login_required(DetalleProveedor), name="ver_notas_super"),
    url(r'^aplicacion/ver_notas_super_2/(?P<pk>\d+)/(?P<estatus>\d+)$',login_required(DetalleProveedor_2), name="ver_notas_super2"),
    url(r'^aplicacion/retiro/(?P<pk>\d+)/$',login_required(retiro), name="retiro"),
    url(r'^aplicacion/pasar_nivel/$',login_required(pasar_nivel), name="pasar_nivel"),
    url(r'^aplicacion/pdf_nivel1/$',login_required(nivel1_pdf.as_view()), name="reporte_nivel1"),
    url(r'^aplicacion/estudiantes/$',login_required(Estudiantes.as_view()), name="estudiante"),
    url(r'^aplicacion/notas_p/$',login_required(Notas_P.as_view()), name="notas_p"),


    url(r'^aplicacion/pdf_nivel2/$',login_required(nivel2_pdf.as_view()), name="reporte_nivel2"),
    url(r'^aplicacion/pdf_nivel3/$',login_required(nivel3_pdf.as_view()), name="reporte_nivel3"),
    url(r'^aplicacion/editar_nota/(?P<pk>\d+)/$',login_required(updateNota.as_view()), name="editar_nota"),
    url(r'^aplicacion/cambiar_profesor/(?P<pk>\d+)/$',login_required(UpdateMateria.as_view()), name="cambiar_profesor"),
    url(r'^aplicacion/terminar_n/(?P<pk>\d+)/$',login_required(terminar), name="terminar"),






]