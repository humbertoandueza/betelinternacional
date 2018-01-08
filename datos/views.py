# -*- coding: utf-8 -*-
from django.shortcuts import render,get_object_or_404
from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse_lazy
from datos import helpers
from django.views.generic import ListView, CreateView,View,UpdateView,DeleteView
from django.http import HttpResponse, HttpResponseRedirect
from .forms import *
from .models import *
from django.contrib.auth.models import User
from accounts.models import Users
from django.conf import settings
from django.db.models import Count
from django.template import RequestContext
from django.shortcuts import render_to_response
from itertools import chain
import json
from io import BytesIO
from django.db.models import Sum
from reportlab.pdfgen import canvas

from reportlab.lib.units import inch, cm
from reportlab.platypus import Table, TableStyle,Image
from reportlab.lib import colors
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from django.contrib.auth.decorators import permission_required
"""

from aplicacion.utils import render_to_pdf
"""

def home(request,pk): # Por favor pon nombres descriptivos
    # Objeto creado en memoria
    # No sera guardado en la db hasta que se lo indiques
    # Ojo aqui nunca le indico que lo guarde
    prueba = get_object_or_404(Profesor,pk=pk)
    return render(request,'aplicacion/aplicacion_nota.html',{'prueba':prueba})

def index(request):
	return render(request,'index.html')

def app_index(request):
	filtro = Asigna_Materia.objects.filter(profesor_id=request.user.ci)
	print (filtro)
	return render(request,'aplicacion/paneladminnw.html', {"filtro":filtro})
#@permission_required('auth.add_user', login_url='accounts/login/')

class notas(ListView):
	model = Notas
	template_name = 'aplicacion/notas_list.html'


def notas_filter(request):
	nota = Notas.objects.filter(cedula_id=request.user.ci)
	var = nota.aggregate(total=Sum('nota_persona'))
	print (var)
	return render(request, "aplicacion/notas_list.html", {"notas":nota,"total":var})

def nivel1_new(request):
	nivel = Inscripcion.objects.filter(id_nivel_id=1)
	nivel1 = len(Inscripcion.objects.filter(id_nivel_id=1))
	print (nivel1)
	filtro = Asigna_Materia.objects.get(profesor_id=request.user.ci)
	print ('njksndkjs',filtro)
	paginator = Paginator(nivel, 5)
	page = request.GET.get("page", 1)
	try:
		nivel = paginator.page(page)
	except PageNotAnInteger:
		nivel = paginator.page(1)
	except EmptyPage:
		nivel = paginator.page(paginator.num_pages)
	buscador = request.GET
	#print (buscador)
	if "q" in buscador:
		query = request.GET["q"]
		if query == "":
			return redirect ('dato:nivel1')
		#querys = (Q(cedula__icontains=query))
		nivel = Inscripcion.objects.filter(cedula_id=query)
		#print (nivel)

		if len(nivel) == 0:
			nivel = Inscripcion.objects.filter(cedula_id=query)
		else:
			return render(request,'aplicacion/nivel1.html', {'nivel1':nivel1,"filtro":filtro,"nivel":nivel})
	return render(request,'aplicacion/nivel1.html', {'nivel1':nivel1,"filtro":filtro,"nivel":nivel})

def nivel2_new(request):
	nivel = Inscripcion.objects.filter(id_nivel_id=2)
	nivel1 = len(Inscripcion.objects.filter(id_nivel_id=2))
	print (nivel1)
	filtro = Asigna_Materia.objects.get(profesor_id=request.user.ci)
	print ('njksndkjs',filtro)
	paginator = Paginator(nivel, 6)
	page = request.GET.get("page", 1)
	try:
		nivel = paginator.page(page)
	except PageNotAnInteger:
		nivel = paginator.page(1)
	except EmptyPage:
		nivel = paginator.page(paginator.num_pages)
	buscador = request.GET
	#print (buscador)
	if "q" in buscador:
		query = request.GET["q"]
		if query == "":
			return redirect ('dato:nivel2')
		#querys = (Q(cedula__icontains=query))
		nivel = Inscripcion.objects.filter(cedula_id=query)
		#print (nivel)

		if len(nivel) == 0:
			nivel = Inscripcion.objects.filter(cedula_id=query)
		else:
			return render(request,'aplicacion/nivel2.html', {'nivel1':nivel1,"filtro":filtro,"nivel":nivel})
	return render(request,'aplicacion/nivel2.html', {'nivel1':nivel1,"filtro":filtro,"nivel":nivel})

class nivel1(ListView):
	model = Inscripcion
	template_name = 'aplicacion/nivel1.html'
	paginate_by= 2

"""
def notas(request):
	buscador = request.GET
	notas = Notas.objects.all()

	if "q65323ndmbshdsdsytd4347" in buscador:
		query = request.GET["q65323ndmbshdsdsytd43473"]
		if query == "" or query == " ":
			mensaje = "Ingrese cédula, nombre o apellido para q."
		else:
			if len(query) < 0:
				mensaje= "Dato invalido."
			else:
				querys = (Q(cedula__cedula__icontains=query))
				nota = Notas.objects.filter(querys)
				if len(notas) == 0:
					mensaje= "No hay resultados para la busqueda."
					nota = Notas.objects.all()
				else:
					return render(request, "aplicacion/notas_list.html", {"notas":nota})

	return render(request, "aplicacion/notas_list.html", {"notas":notas})
"""
class nivel2(ListView):
	model = Inscripcion
	template_name = 'aplicacion/nivel2.html'

class nivel3(ListView):
	model = Inscripcion
	template_name = 'aplicacion/nivel3.html'

class SolicitudListPro(ListView):
	model = Persona
	template_name = 'aplicacion/aplicacion_listpro.html'


def buscar(request,pk):
	cliente=get_object_or_404(Persona,pk=pk)
	return render(request, 'aplicacion/lista.html',{'cliente': cliente})


class NivelCreate(CreateView):
	model = Nivel
	template_name = 'aplicacion/nivel_form.html'
	form_class = NivelForm
	success_url = reverse_lazy('dato:app_inicio')

def ConfirmarInscripcion(request):
    return render(request, 'aplicacion/confirmarinscripcion.html')

class InscripcionCreate(CreateView):
	model = Inscripcion
	template_name = 'aplicacion/inscripcion_form.html'
	form_class = InscripcionForm
	success_url = reverse_lazy('dato:confirmar1')

class ProfesorCreate(CreateView):
	model = Profesor
	template_name = 'aplicacion/profesor_form.html'
	form_class = ProfesorForm
	success_url = reverse_lazy('dato:app_inicio')

class MateriaCreate(CreateView):
	model = Materia
	template_name = 'aplicacion/materia_form.html'
	form_class = MateriaForm
	success_url = reverse_lazy('dato:app_inicio')

class NotaCreate(CreateView):
	template_name = 'aplicacion/nota_form.html'
	form_class = NotasForm
	success_url = reverse_lazy('dato:nivel1')

	def dispatch(self, *args, **kwargs):
		self.cedula_id = kwargs['pk']
		var = self.cedula_id
		print (var)

		context= super(NotaCreate, self).dispatch(*args, **kwargs)
		print (context)
		return context

def post_new(request,*args, **kwargs):
	cedula = kwargs['pk']
	#print (cedula1)
	if request.user.is_profesor:
		filtro = Asigna_Materia.objects.get(profesor_id=request.user.ci)
		var = filtro.materia_id
	filtro2 = Materia.objects.get(id_materia=var)
	var2= filtro2.id_nivel_id
	#print (var2)
	#print (var)
	nivel = Inscripcion.objects.filter(id_nivel_id=var2,cedula_id=cedula)
	if nivel:
		print ('djksdns')
	else:
		print ('error')


	#print(nivel)
	filtro1  = Persona.objects.filter(cedula=cedula)
	#print (filtro1)
	nota = Notas.objects.filter(id_materia_id=filtro.id,cedula_id=cedula)
	#print (nota)
	nota3 = len(nota)
	nota4 = nota3 + 1
	#print (nota3)
	#print (nota)
	#print (filtro1)
	if request.method == 'POST':
		form = NotasForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('dato:nivel1')
	else:
		form = NotasForm()
	return render(request, 'aplicacion/nota_form.html', {'nivel':nivel, 'nota4':nota4,'filtro1':filtro1,'nota3':nota3,'form':form,'cedula':cedula,'filtro':filtro})

class SolicitudCreate(CreateView):
	model = Persona
	template_name = 'aplicacion/aplicacion_form1.html'
	form_class = PersonaForm
	success_url = reverse_lazy('dato:inscripcion')


	def get_context_data(self, **kwargs):
		context = super(SolicitudCreate, self).get_context_data(**kwargs)
		if 'form' not in context:
			context['form'] = self.form_class(self.request.GET)
		return context

	def post(self, request, *args, **kwargs):
		self.object = self.get_object
		form = self.form_class(request.POST)
		if form.is_valid():
			solicitud = form.save()
			solicitud.save()

			return HttpResponseRedirect(self.get_success_url())
		else:
			return self.render_to_response(self.get_context_data(form=form))


class SolicitudUpdate(UpdateView):
	model = Persona
	template_name = 'aplicacion/aplicacion_form1.html'
	form_class = PersonaForm
	success_url = reverse_lazy('dato:app_inicio')



class SolicitudDelete(DeleteView):
	model = Persona
	template_name = 'aplicacion/aplicacion_delete.html'
	success_url = reverse_lazy('dato:app_inicio')


class ReportePersonasPDF(View):

	def cabecera(self,pdf):
	        #Utilizamos el archivo logo_django.png que está guardado en la carpeta media/imagenes
	        archivo_imagen = '/home/humberto/betelinternacional/static/assets/ico/logo.png'
	       	pdf.drawImage(archivo_imagen, 60, 750, width=80,height=80,preserveAspectRatio=True)
	       	pdf.setFont("Helvetica", 16)
	       	pdf.drawString(210, 790, u"Iglesia Bet-el Internacional")
	       	pdf.setFont("Helvetica", 14)
	       	pdf.drawString(160, 770, u"Reportes de personas Inscritas en la escuela de ")
	       	pdf.drawString(230, 750, u"Formacion y Discipulado")
	       	pdf.drawString(250, 720, u"1er Nivel")



	def tabla(self,pdf,y):
	        #Creamos una tupla de encabezados para neustra tabla
	        encabezados = ('Cedula', 'Nombre', 'Apellido', 'Sexo')
	        #Creamos una lista de tuplas que van a contener a las personas
	        detalles = [(Persona.cedula, Persona.nombre, Persona.apellido, Persona.sexo) for Persona in Persona.objects.all()]
	        #Establecemos el tamaño de cada una de las columnas de la tabla
	        detalle_orden = Table([encabezados] + detalles, colWidths=[2 * cm, 3 * cm, 3 * cm, 4 * cm])
	        #Aplicamos estilos a las celdas de la tabla
	        detalle_orden.setStyle(TableStyle([('ALIGN',(1,1),(1,1),'CENTER'),
	     			('INNERGRID', (0,0), (-1,-1), 0.25, colors.black),
                    ('BOX', (0,0), (-1,-1), 0.25, colors.black),]))
	        #Establecemos el tamaño de la hoja que ocupará la tabla
	        detalle_orden.wrapOn(pdf, 380, 580)
	        #Definimos la coordenada donde se dibujará la tabla
	        detalle_orden.drawOn(pdf, 70,y)

	def get(self, request, *args, **kwargs):
	        #Indicamos el tipo de contenido a devolver, en este caso un pdf
	        response = HttpResponse(content_type='application/pdf')
	        #La clase io.BytesIO permite tratar un array de bytes como un fichero binario, se utiliza como almacenamiento temporal
	        buffer = BytesIO()
	        #Canvas nos permite hacer el reporte con coordenadas X y Y
	        pdf = canvas.Canvas(buffer)
	        #Llamo al método cabecera donde están definidos los Persona que aparecen en la cabecera del reporte.
	        self.cabecera(pdf)
	        y = 300
	        self.tabla(pdf, y)
	        #Con show page hacemos un corte de página para pasar a la siguiente
	        pdf.showPage()
	        pdf.save()
	        pdf = buffer.getvalue()
	        buffer.close()
	        response.write(pdf)
	        return response

"""
def GeneratePdf(self,*args, **kwargs):
	pdf = Persona
    dato = {'pdf': pdf }
    pdf2 = render_to_pdf('pdf/invoce.html',dato)
    return HttpResponse(pdf2, content_type='application/pdf')"""

