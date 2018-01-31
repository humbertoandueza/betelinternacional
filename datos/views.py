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

from io import BytesIO

from reportlab.platypus import SimpleDocTemplate, Paragraph, TableStyle,PageBreak
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.platypus import Table
from reportlab.pdfgen import canvas
from reportlab.lib.units import mm
from reportlab.lib.units import inch


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
	#print (filtro)
	if request.user.is_alumno and not request.user.is_inscripcion:
		notificacion = Notificacion.objects.filter(user_id=request.user.ci).order_by('-hora','-id')

		notificaciones = Notificacion.objects.filter(user_id=request.user.ci,estatus=False)
		var = len(notificaciones)

		return render(request,'aplicacion/paneladminnw.html', {'var':var,"filtro":filtro,'notificacion':notificacion})

	return render(request,'aplicacion/paneladminnw.html', {"filtro":filtro})
#@permission_required('auth.add_user', login_url='accounts/login/')
def notificaciones(request):
	if request.user.is_alumno and not request.user.is_inscripcion:
		notificacion = Notificacion.objects.filter(user_id=request.user.ci).order_by('-hora','-id')

		notificaciones = Notificacion.objects.filter(user_id=request.user.ci,estatus=False)
		var = len(notificaciones)
	return render(request,'aplicacion/notificacion.html', {'var':var,'notificacion':notificacion})

def push_notificaciones(request):
	if request.user.is_alumno and not request.user.is_inscripcion:
		notificacion = Notificacion.objects.filter(user_id=request.user.ci).order_by('-hora','-id')

		notificaciones = Notificacion.objects.filter(user_id=request.user.ci,estatus=False)
		var = len(notificaciones)
	return render(request,'aplicacion/notificaciones.html', {'var':var,'notificacion':notificacion})

def notificacion(request,pk):
	notificaciones = Notificacion.objects.filter(pk=pk).update(estatus=True)
	return redirect('dato:app_inicio')

class notas(ListView):
	model = Notas
	template_name = 'aplicacion/notas_list.html'


def notas_filter(request):
	inscripcion1 = get_object_or_404(Inscripcion,cedula_id=request.user.ci)
	filtro = inscripcion1.id_nivel_id
	materias = Materia.objects.filter(id_nivel_id=filtro)
	print (materias)
	if filtro == 1:
		#calculo de notas y saber cuantas notas van cargadas en familia
		notas = Notas.objects.filter(cedula_id=request.user.ci,id_materia_id=1)
		cantidad12 = len(notas)
		if cantidad12 != 0:

			calculo = Notas.objects.filter(cedula_id=request.user.ci,id_materia_id=1).aggregate(total=Sum('nota_persona'))
			print ('la cantidad de las notas cargadas en familia son ',cantidad12)
			for p in calculo.items():
				cantidad = (int(p[1]))
			print ('la nota de familia es', cantidad)
			if cantidad12 >= 9 and cantidad >= 7:
				print ('aprobado')
		#calculo de notas y saber cuantas notas van cargadas en fundamento
		notas1 = Notas.objects.filter(cedula_id=request.user.ci,id_materia_id=2)
		cantidad13 = len(notas1)
		if cantidad13:
			calculo1 = Notas.objects.filter(cedula_id=request.user.ci,id_materia_id=2).aggregate(total=Sum('nota_persona'))
			print ('la cantidad de las notas cargadas en fundameno son ',cantidad13)
			for p in calculo1.items():
				cantidad1 = (int(p[1]))
			print ('la nota de fundamento es', cantidad1)
			estatus = ''
			if cantidad13 >= 9 and cantidad1 >= 7:
				estatus = 'Aprobado'
			elif cantidad13 >=9 and cantidad1 < 7:
				estatus = 'Reprobado'
			nota = Notas.objects.filter(cedula_id=request.user.ci)
			return render(request, "aplicacion/notas_list.html", {'estatus':estatus,'inscripcion1':inscripcion1,"notas":nota,})

	nota = Notas.objects.filter(cedula_id=request.user.ci)

	return render(request, "aplicacion/notas_list.html", {'inscripcion1':inscripcion1,"notas":nota,})

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

	def form_valid(self, form):
		datos= form.save(commit=False)
		datos.cedula_id = self.kwargs['pk']
		datos.save()

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
	calculo = Notas.objects.filter(cedula_id=cedula).aggregate(total=Sum('nota_persona'))
	#print (nota)
	nota_total = Notas.objects.filter(cedula_id=cedula)
	carga_total = len(nota_total)
	nota3 = len(nota)
	nota4 = nota3 + 1
	if nota3 != 0:
		for p in calculo.items():
			cantidad = (int(p[1]))
		print ('Nota total', cantidad)
		if cantidad >= 14 and carga_total >= 18 :
			Inscripcion.objects.filter(pk=cedula).update(estatus=True)
		elif cantidad <14 and carga_total > 17 :
			Inscripcion.objects.filter(pk=cedula).update(estatus=False)
	print (' cantidad de notas cargadas, ',carga_total)
	#print (nota)
	#print (filtro1)
	if request.method == 'POST':
		print ('LOS VALORES RECIBIDOS', request.POST)
		form = NotasForm(request.POST)
		if form.is_valid():
			form.save()
			noto = {
				'titulo': 'Carga de nota',
				'descripcion': 'Se le ha cargado una nueva nota',
				'estatus': False,
				'user': cedula,
			}
			notificaciones =NotificacionesForm(noto)
			print (noto)
			notificaciones.save()
			#print (notificaciones)
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
	        archivo_imagen = 'C:/Users/equi/betelinternacional/static/assets/img/logo1.png'
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
	        if len(detalles) > 10:
	        	buffer = BytesIO()
	        	self.cabecera(pdf)

	       		pdf = canvas.Canvas(buffer)

	        	pdf.showPage()
	        	pdf.write()
	        	
	        	buffer.close()

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

	def get(self, request,*args, **kwargs):
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
	        print (self.tabla)	
	        pdf.showPage()
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

class generar_pdf(View):
	def _header_footer(self,canvas,doc):
		canvas.saveState()
		styles = getSampleStyleSheet()
		archivo_imagen = 'C:/Users/equi/betelinternacional/static/assets/img/gif.gif'
		canvas.drawImage(archivo_imagen, 60, 700, width=75,height=75,preserveAspectRatio=True)
		#iglesia
		header1 = Paragraph('Iglesia Cristiana Bet-el Internacional', styles['Heading4'])
		w, h = header1.wrap(doc.width-120, doc.topMargin)
		header1.drawOn(canvas, 210, doc.height + doc.topMargin - 6)
		#ministerio
		header = Paragraph('Ministerio de Educacion Cristiana', styles['Heading4'])
		w, h = header.wrap(doc.width-120, doc.topMargin)
		header.drawOn(canvas, 220, doc.height + doc.topMargin - 30)
		#escuela
		header = Paragraph('Escuela de Formación y Discipulado', styles['Heading4'])
		w, h = header.wrap(doc.width-120, doc.topMargin)
		header.drawOn(canvas, 210, doc.height + doc.topMargin - 18)
		#guananare
		header = Paragraph('Guanare-Portuguesa', styles['Heading4'])
		w, h = header.wrap(doc.width-120, doc.topMargin)
		header.drawOn(canvas, 250, doc.height + doc.topMargin - 41)
		footer = Paragraph('Iglesia Cristiana Bet-el Internacional', styles['Normal'])
		w, h = footer.wrap(doc.width, doc.bottomMargin)
		footer.drawOn(canvas, doc.leftMargin, h)
		canvas.restoreState()

	def get(self,request):
	    print ("Genero el PDF")
	    response = HttpResponse(content_type='application/pdf')
	    pdf_name = "clientes.pdf"  # llamado clientes
	    # la linea 26 es por si deseas descargar el pdf a tu computadora
	    # response['Content-Disposition'] = 'attachment; filename=%s' % pdf_name
	    buff = BytesIO()
	    doc = SimpleDocTemplate(buff,
	    						pagesize=letter,
	    						rightMargin=40,
	    						leftMargin=40,
	    						topMargin=95,
	    						bottomMargin=40,
	    						)
	    if request.user.is_superuser:
		    clientes = []
		    styles = getSampleStyleSheet()
		    header=Paragraph('Lista de usuarios registrados',styles['Heading1'])
		    clientes.append(header)
		    headings = ('Cedula','Nombre', 'Apellido', 'Correo')
		    allclientes = [(p.ci,p.first_name, p.last_name, p.email) for p in Users.objects.all()]
		    t = Table([headings] + allclientes)
		    t.setStyle(TableStyle(
		    	[	('GRID', (0, 0), (3, -1), 1, colors.black),
		    	('LINEBELOW', (0, 0), (-1, 0), 2, colors.black),
		    	('BACKGROUND', (0, 0), (-1, 0), colors.dodgerblue)
		    	]
		    	))
		    #clientes.append(t)
		    clientes.append(t)
		    doc.build(clientes,onFirstPage=self._header_footer,onLaterPages=self._header_footer,canvasmaker=NumberedCanvas)
	    else:
		    clientes = []
		    styles = getSampleStyleSheet()
		    header=Paragraph('Lista de usuarios registrados',styles['Heading1'])
		    clientes.append(header)
		    doc.build(clientes,onFirstPage=self._header_footer,onLaterPages=self._header_footer,canvasmaker=NumberedCanvas)
	    response.write(buff.getvalue())
	    buff.close()
	    return response

class generar_pdf_personal(View):
	def _header_footer(self,canvas,doc):
		canvas.saveState()
		styles = getSampleStyleSheet()
		archivo_imagen = 'C:/Users/equi/betelinternacional/static/assets/img/gif.gif'
		canvas.drawImage(archivo_imagen, 60, 700, width=75,height=75,preserveAspectRatio=True)
		#iglesia
		header1 = Paragraph('Iglesia Cristiana Bet-el Internacional', styles['Heading4'])
		w, h = header1.wrap(doc.width-120, doc.topMargin)
		header1.drawOn(canvas, 210, doc.height + doc.topMargin - 6)
		#ministerio
		header = Paragraph('Ministerio de Educacion Cristiana', styles['Heading4'])
		w, h = header.wrap(doc.width-120, doc.topMargin)
		header.drawOn(canvas, 220, doc.height + doc.topMargin - 30)
		#escuela
		header = Paragraph('Escuela de Formación y Discipulado', styles['Heading4'])
		w, h = header.wrap(doc.width-120, doc.topMargin)
		header.drawOn(canvas, 210, doc.height + doc.topMargin - 18)
		#guananare
		header = Paragraph('Guanare-Portuguesa', styles['Heading4'])
		w, h = header.wrap(doc.width-120, doc.topMargin)
		header.drawOn(canvas, 250, doc.height + doc.topMargin - 41)
		footer = Paragraph('Iglesia Cristiana Bet-el Internacional', styles['Normal'])
		w, h = footer.wrap(doc.width, doc.bottomMargin)
		footer.drawOn(canvas, doc.leftMargin, h)
		canvas.restoreState()

	def get(self,request,pk):
	    print ("Genero el PDF")
	    response = HttpResponse(content_type='application/pdf')
	    pdf_name = "clientes.pdf"  # llamado clientes
	    # la linea 26 es por si deseas descargar el pdf a tu computadora
	    # response['Content-Disposition'] = 'attachment; filename=%s' % pdf_name
	    buff = BytesIO()
	    doc = SimpleDocTemplate(buff,
	    						pagesize=letter,
	    						rightMargin=40,
	    						leftMargin=40,
	    						topMargin=110,
	    						bottomMargin=40,
	    						)
	    if request.user.is_superuser:
		    clientes = []
		    styles = getSampleStyleSheet()
		    header=Paragraph('Reporte Personal',styles['Heading1'])
		    header1=Paragraph('Datos Personales',styles['Heading2'])
		    clientes.append(header)
		    clientes.append(header1)
		    allclientes = get_object_or_404(Inscripcion,pk=pk)
		    #TABLA NUMERO 1
		    headings = ('   Cedula      ','    Nombre   ', '    Apellido    ', 'Dirección                                                                                                             ')
		    lista = (allclientes.cedula_id,allclientes.cedula.nombre,allclientes.cedula.apellido,allclientes.cedula.direccion)
		    t = Table([headings] + [lista])
		    t.setStyle(TableStyle(
		    	[	('GRID', (0, 0), (3, -1), 1, colors.black),
		    	('LINEBELOW', (0, 0), (-1, 0), 2, colors.black),
		    	('BACKGROUND', (0, 0), (-1, 0), colors.lightblue)
		    	]
		    	))
		    clientes.append(t)
		    header21=Paragraph('',styles['Heading2'])
		    clientes.append(header21)
		    #TABLA NUMERO 2
		    headings1 = ('Fecha de nacimiento','Sexo    ', 'Telefono residencial    ', 'Telefono Celular       ','Email                                                    ')
		    lista1 = (allclientes.cedula.fecha_de_nacimiento,allclientes.cedula.sexo,allclientes.cedula.telefono_residencial,allclientes.cedula.celular+ allclientes.cedula.celular_number,allclientes.cedula.email)
		    t1 = Table([headings1] + [lista1])
		    t1.setStyle(TableStyle(
		    	[	('GRID', (0, 0), (5, -1), 1, colors.black),
		    	('LINEBELOW', (0, 0), (-1, 0), 2, colors.black),
		    	('BACKGROUND', (0, 0), (-1, 0), colors.lightblue)
		    	]
		    	))
		    clientes.append(t1)
		    #DATOS SOCIOECONOMICOS
		    header31=Paragraph('Datos Socioeconomicos',styles['Heading2'])
		    clientes.append(header31)
		    headings2 = ('Estado Civil   ','Trabaja    ', 'Profesion             ', 'Origen de Estudio       ','Ingreso Familiar                                                    ')
		    lista2 = (allclientes.cedula.estado_civil,allclientes.cedula.trabaja,allclientes.cedula.profesion,allclientes.cedula.estudio_ori,allclientes.cedula.ing_famil)
		    t2 = Table([headings2] + [lista2])
		    t2.setStyle(TableStyle(
		    	[	('GRID', (0, 0), (5, -1), 1, colors.black),
		    	('LINEBELOW', (0, 0), (-1, 0), 2, colors.black),
		    	('BACKGROUND', (0, 0), (-1, 0), colors.lightblue)
		    	]
		    	))
		    clientes.append(t2)
		    #DATOS ECLESIASTICOS
		    header41=Paragraph('Datos Eclesiasticos',styles['Heading2'])
		    clientes.append(header41)
		    headings3 = ('Iglesia   ','Pastor    ', 'Estudio Teologico             ', 'Instituto                      ','Titulo Obtenido                                                    ')
		    lista3 = (allclientes.cedula.iglesia,allclientes.cedula.pastor,allclientes.cedula.estudio_teo,allclientes.cedula.instituto,allclientes.cedula.titulo_obte)
		    t3 = Table([headings3] + [lista3])
		    t3.setStyle(TableStyle(
		    	[	('GRID', (0, 0), (5, -1), 1, colors.black),
		    	('LINEBELOW', (0, 0), (-1, 0), 2, colors.black),
		    	('BACKGROUND', (0, 0), (-1, 0), colors.lightblue)
		    	]
		    	))
		    clientes.append(t3)
		    header43=Paragraph('',styles['Heading2'])
		    clientes.append(header43)
		    headings4 = ('Actividad que realiza en la iglesia                    ','Ministerio en el desea participar    ', 'Razon por la cual estudiará                 ')
		    lista4 = (allclientes.cedula.actividad,allclientes.cedula.ministerio,allclientes.cedula.razon)
		    t4 = Table([headings4] + [lista4])
		    t4.setStyle(TableStyle(
		    	[	('GRID', (0, 0), (5, -1), 1, colors.black),
		    	('LINEBELOW', (0, 0), (-1, 0), 2, colors.black),
		    	('BACKGROUND', (0, 0), (-1, 0), colors.lightblue)
		    	]
		    	))
		    clientes.append(t4)

		    doc.build(clientes,onFirstPage=self._header_footer,onLaterPages=self._header_footer,canvasmaker=NumberedCanvas)
	    else:
		    clientes = []
		    styles = getSampleStyleSheet()
		    header=Paragraph('Lista de usuarios registrados',styles['Heading1'])
		    clientes.append(header)
		    doc.build(clientes,onFirstPage=self._header_footer,onLaterPages=self._header_footer,canvasmaker=NumberedCanvas)
	    response.write(buff.getvalue())
	    buff.close()
	    return response
class NumberedCanvas(canvas.Canvas):


    def __init__(self, *args, **kwargs):
        canvas.Canvas.__init__(self, *args, **kwargs)
        self._saved_page_states = []
 

    def showPage(self):
        self._saved_page_states.append(dict(self.__dict__))
        self._startPage()
 

    def save(self):
        """add page info to each page (page x of y)"""
        num_pages = len(self._saved_page_states)
        for state in self._saved_page_states:
            self.__dict__.update(state)
            self.draw_page_number(num_pages)
            canvas.Canvas.showPage(self)
        canvas.Canvas.save(self)
 
 
    def draw_page_number(self, page_count):
    	self.setFont("Helvetica", 9)
    	self.drawRightString(211 * mm, 4 * mm + (0.1 * inch),"Pagina %d de %d" % (self._pageNumber, page_count))