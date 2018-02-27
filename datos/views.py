# -*- coding: utf-8 -*-
from django.shortcuts import render,get_object_or_404
from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse_lazy
from datos import helpers
from django.views.generic import ListView, CreateView,View,UpdateView,DeleteView,DetailView
from django.http import HttpResponse, HttpResponseRedirect
from .forms import *
from .models import *
from django.contrib.auth.models import User
from accounts.models import Users
from accounts.forms import *
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

from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm

from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from django.contrib.auth.decorators import permission_required
import datetime
import time

def index(request):
	return render(request,'index.html')


def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect('dato:app_inicio')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'aplicacion/change_password.html', {
        'form': form
    })


def app_index(request):
	filtro = Asigna_Materia.objects.filter(profesor_id=request.user.ci)
	#print (filtro)
	if request.user.is_alumno and not request.user.is_inscripcion and not request.user.is_superuser:
		notificacion = Notificacion.objects.filter(titulo='Carga de nota',user_id=request.user.ci).order_by('-hora','-id')
		inscripcion1 =Inscripcion.objects.filter(cedula_id=request.user.ci,estatus=0,terminado=False)
		for i in inscripcion1:
			form = str(i.id_nivel_id)
			nivel = Nivel.objects.get(id_nivel=form)
			var1= nivel.nivel
			print (var1)
		notificaciones = Notificacion.objects.filter(titulo='Carga de nota',user_id=request.user.ci,estatus=False)
		var = len(notificaciones)
		if inscripcion1:
			return render(request,'aplicacion/paneladminnw.html', {'var1':var1,'inscripcion1':inscripcion1,'var':var,"filtro":filtro,'notificacion':notificacion})
			
		return render(request,'aplicacion/paneladminnw.html', {'var':var,"filtro":filtro,'notificacion':notificacion})
	if request.user.is_superuser:
		notificacion = Notificacion.objects.filter(titulo='Retiro').order_by('-hora','-id')

		notificaciones = Notificacion.objects.filter(titulo='Retiro',estatus=False)
		var = len(notificaciones)

		return render(request,'aplicacion/paneladminnw.html', {'var':var,"filtro":filtro,'notificacion':notificacion})

	return render(request,'aplicacion/paneladminnw.html', {"filtro":filtro})

def notificacion(request,pk):
	notificaciones = Notificacion.objects.filter(pk=pk).update(estatus=True)
	return redirect('dato:app_inicio')

def notas_filter(request):
	if request.user.is_alumno and not request.user.is_superuser:
		inscripcion2 = Inscripcion.objects.filter(cedula_id=request.user.ci)
		for i in inscripcion2:
			if i.estatus != 2:
				estatus = i.estatus
		inscripcion1 = get_object_or_404(Inscripcion,cedula_id=request.user.ci,estatus=estatus,terminado=False)
		filtro = inscripcion1.id_nivel_id
		materias = Materia.objects.filter(id_nivel_id=filtro)
		if len(materias) < 2:
			print ("error")
		else:
			id_materia1 = materias[0]
			id_materia2 = materias[1]
			obtener_id1 = id_materia1.id_materia
			obtener_id2 = id_materia2.id_materia

			print ('id de la materia: ',id_materia1 ,'es : ',obtener_id1)
			print ('id de la materia: ',id_materia2 ,'es : ',obtener_id2)
		if filtro :
			#calculo de notas y saber cuantas notas van cargadas en familia
			notas = Notas.objects.filter(cedula_id=inscripcion1.id,id_materia_id=obtener_id1)
			cantidad12 = len(notas)
			print ('notas',cantidad12)
			if cantidad12 != 0:

				calculo = Notas.objects.filter(cedula_id=inscripcion1.id,id_materia_id=obtener_id1).aggregate(total=Sum('nota_persona'))
				print ('la cantidad de las notas cargadas en familia son ',cantidad12)
				for p in calculo.items():
					cantidad = (int(p[1]))
				print ('la nota de familia es', cantidad)
				
			#calculo de notas y saber cuantas notas van cargadas en fundamento
			notas1 = Notas.objects.filter(cedula_id=inscripcion1.id,id_materia_id=obtener_id2)
			print ('notas23232', notas1)
			cantidad13 = len(notas1)
			if cantidad13:
				calculo1 = Notas.objects.filter(cedula_id=inscripcion1.id,id_materia_id=obtener_id2).aggregate(total=Sum('nota_persona'))
				print ('la cantidad de las notas cargadas en fundameno son ',cantidad13)
				for p in calculo1.items():
					cantidad1 = (int(p[1]))
				print ('la nota de fundamento es', cantidad1)
			materia1 = id_materia1.nombre_materia
			materia2 = id_materia2.nombre_materia
			estatus1 = 'Indefinido'
			if cantidad12 >= 9 and cantidad > 7:
				estatus1 = 'Aprobado'
			elif cantidad12 >=9 and cantidad <= 7:
				estatus1 = 'Reprobado'
			estatus = 'Indefinido'
			if cantidad13 >= 9 and cantidad1 >7:
				estatus = 'Aprobado'
			elif cantidad13 >=9 and cantidad1 <= 6:
				estatus = 'Reprobado'
			nota = Notas.objects.filter(cedula_id=request.user.ci)
			return render(request, "aplicacion/notas_list.html", {'cantidad12':cantidad12,'cantidad13':cantidad13, 'materia1':materia1,'materia2':materia2, 'estatus':estatus,'estat':estatus1,'inscripcion1':inscripcion1,"notas":notas,"notas1":notas1,})

		estatus = 'no defined'
		return render(request, "aplicacion/notas_list.html", {'inscripcion1':inscripcion1,"notas":nota,})
	else :
		return redirect('dato:app_inicio')


def DetalleProveedor(request,pk):
	inscripcion = get_object_or_404(Inscripcion,id=pk,terminado=False)
	profesor =get_object_or_404(Asigna_Materia,profesor_id=request.user.ci)
	notas = Notas.objects.filter(cedula_id=pk,id_materia_id=profesor.materia_id)
	if notas:
		notas_sumas  = Notas.objects.filter(cedula_id=pk,id_materia_id=profesor.materia_id).aggregate(total=Sum('nota_persona'))
		estatus= ''
		for p in notas_sumas.items():
			cantidad = (int(p[1]))
			if  cantidad > 7:
					estatus = 'Aprobado'
			elif cantidad <= 7:
				estatus = 'Reprobado'
		return render(request,'aplicacion/ver_notas_profesor.html',{'estatus':estatus,'notas':notas,'alumno':inscripcion})
	else:
		estatus = 'El alumno no posee notas cargadas'
		return render(request,'aplicacion/ver_notas_profesor.html',{'estatus':estatus})

def DetalleProveedor_2(request,pk,estatus=None):
	if request.user.is_superuser:
		inscripcion1 = get_object_or_404(Inscripcion,cedula_id=pk,estatus=estatus,terminado=False)
		filtro = inscripcion1.id_nivel_id
		print (inscripcion1)
		materias = Materia.objects.filter(id_nivel_id=filtro)
		if len(materias) < 2:
			print ("error")
		else:
			id_materia1 = materias[0]
			id_materia2 = materias[1]
			obtener_id1 = id_materia1.id_materia
			obtener_id2 = id_materia2.id_materia

			materia1 = id_materia1.nombre_materia
			materia2 = id_materia2.nombre_materia

			nombre_pro = Asigna_Materia.objects.get(materia_id=obtener_id1)
			nombre1 = nombre_pro.profesor.nombre_profesor
			apellido1 = nombre_pro.profesor.apellido_profesor
			nombre_completo = nombre1+' '+apellido1

			nombre_pro1 = Asigna_Materia.objects.get(materia_id=obtener_id2)
			nombre2 = nombre_pro1.profesor.nombre_profesor
			apellido2 = nombre_pro1.profesor.apellido_profesor
			nombre_completo1 = nombre2+' '+apellido2



		if filtro :
			#calculo de notas y saber cuantas notas van cargadas en familia
			notas = Notas.objects.filter(cedula_id=inscripcion1.id,id_materia_id=obtener_id1)
			if notas:

				cantidad12 = len(notas)
				print ('notas',cantidad12)
				if cantidad12 != 0:

					calculo = Notas.objects.filter(cedula_id=inscripcion1.id,id_materia_id=obtener_id1).aggregate(total=Sum('nota_persona'))
					print ('la cantidad de las notas cargadas en familia son ',cantidad12)
					for p in calculo.items():
						cantidad = (int(p[1]))
					print ('la nota de familia es', cantidad)
				estatus1 = 'Indefinido'
				if  cantidad > 7:
					estatus1 = 'Aprobado'
				elif cantidad <= 7:
					estatus1 = 'Reprobado'
					
				#calculo de notas y saber cuantas notas van cargadas en fundamento
			else:
				cantidad12 = 0
				estatus1 = 'No posee Notas'
			notas1 = Notas.objects.filter(cedula_id=inscripcion1.id,id_materia_id=obtener_id2)
			if notas1:

				print ('notas23232', notas1)
				cantidad13 = len(notas1)
				if cantidad13:
					calculo1 = Notas.objects.filter(cedula_id=inscripcion1.id,id_materia_id=obtener_id2).aggregate(total=Sum('nota_persona'))
					print ('la cantidad de las notas cargadas en fundameno son ',cantidad13)
					for p in calculo1.items():
						cantidad1 = (int(p[1]))
					print ('la nota de fundamento es', cantidad1)
				
				
				estatus = 'Indefinido'
				if cantidad1 >7:
					estatus = 'Aprobado'
				elif cantidad1 <= 7:
					estatus = 'Reprobado'
			else:
				cantidad13 = 0
				estatus ='No posee Notas'
			nota = Notas.objects.filter(cedula_id=pk)
			return render(request, "aplicacion/ver_notas_profesor_super.html", {'nombre_completo':nombre_completo,'nombre_completo1':nombre_completo1,'cantidad12':cantidad12,'cantidad13':cantidad13, 'materia1':materia1,'materia2':materia2, 'estatus':estatus,'estat':estatus1,'inscripcion1':inscripcion1,"notas":notas,"notas1":notas1,})

		estatus = 'no defined'
		return render(request, "aplicacion/ver_notas_profesor_super.html", {'inscripcion1':inscripcion1,"notas":nota,})
	else :
		return redirect('dato:app_inicio')
def pasar_nivel(request):
	if request.method == 'POST':
		inscripcion1 = get_object_or_404(Inscripcion,cedula_id=request.user.ci,estatus=0,terminado=False)
		filtro = inscripcion1.id_nivel_id
		nivel = get_object_or_404(Nivel,id_nivel=filtro)
		avanzar= str(nivel.nivel + 'I')
		nivel_a = get_object_or_404(Nivel,nivel=avanzar)

		print (nivel_a.id_nivel)
		inscripcion = {
			'cedula': request.user.ci,
			'id_nivel': nivel_a.id_nivel,
			'estatus':1,
			}
		inscripciones =InscripcionForm(inscripcion)
		inscripciones.save()
		inscripcion1 = Inscripcion.objects.filter(cedula_id=request.user.ci,estatus=0,terminado=False).update(terminado=True)		
		return redirect('dato:app_inicio')

	return render(request,'aplicacion/retiro.html')

def notas_filter_super(request,pk):
	if request.user.is_superuser or request.user.is_profesor:
		inscripcion1 = get_object_or_404(Inscripcion,cedula_id=pk,estatus=0,terminado=False)
		filtro = inscripcion1.id_nivel_id
		materias = Materia.objects.filter(id_nivel_id=filtro)
		if len(materias) < 2:
			print ("error")
		else:
			id_materia1 = materias[0]
			id_materia2 = materias[1]
			obtener_id1 = id_materia1.id_materia
			obtener_id2 = id_materia2.id_materia

			print ('id de la materia: ',id_materia1 ,'es : ',obtener_id1)
			print ('id de la materia: ',id_materia2 ,'es : ',obtener_id2)
		if filtro :
			#calculo de notas y saber cuantas notas van cargadas en familia
			notas = Notas.objects.filter(cedula_id=inscripcion1.id,id_materia_id=obtener_id1)
			cantidad12 = len(notas)
			print ('notas',cantidad12)
			if cantidad12 != 0:

				calculo = Notas.objects.filter(cedula_id=inscripcion1.id,id_materia_id=obtener_id1).aggregate(total=Sum('nota_persona'))
				print ('la cantidad de las notas cargadas en familia son ',cantidad12)
				for p in calculo.items():
					cantidad = (int(p[1]))
				print ('la nota de familia es', cantidad)
				
			#calculo de notas y saber cuantas notas van cargadas en fundamento
			notas1 = Notas.objects.filter(cedula_id=inscripcion1.id,id_materia_id=obtener_id2)
			print ('notas23232', notas1)
			cantidad13 = len(notas1)
			if cantidad13:
				calculo1 = Notas.objects.filter(cedula_id=inscripcion1.id,id_materia_id=obtener_id2).aggregate(total=Sum('nota_persona'))
				print ('la cantidad de las notas cargadas en fundameno son ',cantidad13)
				for p in calculo1.items():
					cantidad1 = (int(p[1]))
				print ('la nota de fundamento es', cantidad1)
			materia1 = id_materia1.nombre_materia
			materia2 = id_materia2.nombre_materia
			estatus1 = 'Indefinido'
			if cantidad12 >= 9 and cantidad > 7:
				estatus1 = 'Aprobado'
			elif cantidad12 >=9 and cantidad <= 7:
				estatus1 = 'Reprobado'
			estatus = 'Indefinido'
			if cantidad13 >= 9 and cantidad1 >7:
				estatus = 'Aprobado'
			elif cantidad13 >=9 and cantidad1 <= 6:
				estatus = 'Reprobado'
			nota = Notas.objects.filter(cedula_id=request.user.ci)
			return render(request, "aplicacion/notas_list_super.html", {'cantidad12':cantidad12,'cantidad13':cantidad13, 'materia1':materia1,'materia2':materia2, 'estatus':estatus,'estat':estatus1,'inscripcion1':inscripcion1,"notas":notas,"notas1":notas1,})

		estatus = 'no defined'
		return render(request, "aplicacion/notas_list_super.html", {'inscripcion1':inscripcion1,"notas":nota,})
	else :
		return redirect('dato:app_inicio')

def nivel1_new(request):
	if request.user.is_profesor and not request.user.is_superuser:

		filtro = Asigna_Materia.objects.get(profesor_id=request.user.ci)
		filtro1 = filtro.materia_id
		materia = Materia.objects.get(id_materia=filtro1)
		filtro2 = materia.id_nivel_id
		print ('el nivel que esta dando clase es:  ',filtro2)

		nivel = Inscripcion.objects.filter(id_nivel_id=filtro2,estatus__range=["", "1"],terminado=False)
		nivel1 = len(Inscripcion.objects.filter(id_nivel_id=filtro2,estatus__range=["", "1"],terminado=False))
		print (nivel1)
		paginator = Paginator(nivel, 7)
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
				return render(request,'aplicacion/nivel1.html', {'filtro2':filtro2,'nivel1':nivel1,"filtro":filtro,"nivel":nivel})
		return render(request,'aplicacion/nivel1.html', {'filtro2':filtro2,'nivel1':nivel1,"filtro":filtro,"nivel":nivel})
	else:
		return redirect('dato:app_inicio')
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



class InscripcionCreate(CreateView):
	model = Inscripcion
	template_name = 'aplicacion/inscripcion_form.html'
	form_class = InscripcionForm
	success_url = reverse_lazy('dato:confirmar1')

def ProfesorCreate(request):
	if request.method == 'POST':
		form = ProfesorForm(request.POST)
		if form.is_valid():
			Users.objects.filter(ci=request.user.ci).update(is_inscripcion=False)
			form.save()
			return redirect('logout')
	else:
		form = ProfesorForm()
	return render(request,'aplicacion/form_crear_profesor.html',{'form':form})

def AsignarMateria(request,*args,**kwargs):
	if request.method == 'POST':
		form = AsignaMateriaForm(request.POST)
		cedula = (request.POST['profesor'])
		if form.is_valid():
			Profesor.objects.filter(cedula_profesor=cedula).update(estatus=True)
			form.save()
			return redirect('dato:app_inicio')
	else:
		form = AsignaMateriaForm()
	return render(request,'aplicacion/form_asigna_materia.html',{'form':form})

class ListAsignarMateria(ListView):
	model = Asigna_Materia
	template_name = 'aplicacion/list_asigna_materia.html'

def nivel1_superuser(request):
	if request.user.is_superuser:
		nivel = Inscripcion.objects.filter(id_nivel_id=1,estatus__range=["", "1"],terminado=False)
		materias = Materia.objects.filter(id_nivel_id=1)
		if len(materias) < 2:
			print ("error")
		else:
			id_materia1 = materias[0]
			id_materia2 = materias[1]
			obtener_id1 = id_materia1.id_materia
			obtener_id2 = id_materia2.id_materia
			nombre_pro = Asigna_Materia.objects.get(materia_id=obtener_id1)
			nombre1 = nombre_pro.profesor.nombre_profesor
			apellido1 = nombre_pro.profesor.apellido_profesor
			materia1 = id_materia1.nombre_materia
			nombre_completo = 'Profesor: '+nombre1+ ' '+apellido1+ ' Materia: '+materia1 
			print(nombre_completo)

			nombre_pro1 = Asigna_Materia.objects.get(materia_id=obtener_id2)
			nombre2 = nombre_pro1.profesor.nombre_profesor
			apellido2 = nombre_pro1.profesor.apellido_profesor
			materia2 = id_materia2.nombre_materia
			nombre_completo2 = 'Profesor: '+nombre2+ ' '+apellido2+ ' Materia: '+materia2 

			print(nombre_completo2)


		paginator = Paginator(nivel, 7)
		page = request.GET.get("page", 1)
		try:
			nivel = paginator.page(page)
		except PageNotAnInteger:
			nivel = paginator.page(1)
		except EmptyPage:
			nivel = paginator.page(paginator.num_pages)
		buscador = request.GET

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
					return render(request,'aplicacion/nivel1_superuser.html', {"nivel":nivel,})
		return render(request,'aplicacion/nivel1_superuser.html', {'nombre_completo':nombre_completo,'nombre_completo2':nombre_completo2,"nivel":nivel})
	else:
		return redirect('dato:app_inicio')

def nivel2_superuser(request):
	if request.user.is_superuser:
		nivel = Inscripcion.objects.filter(id_nivel_id=2,estatus__range=["", "1"],terminado=False)
		paginator = Paginator(nivel, 7)
		page = request.GET.get("page", 1)
		try:
			nivel = paginator.page(page)
		except PageNotAnInteger:
			nivel = paginator.page(1)
		except EmptyPage:
			nivel = paginator.page(paginator.num_pages)
		buscador = request.GET

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
					return render(request,'aplicacion/nivel1_superuser.html', {"nivel":nivel})
		return render(request,'aplicacion/nivel1_superuser.html', {"nivel":nivel})
	else:
		return redirect('dato:app_inicio')

def nivel3_superuser(request):
	if request.user.is_superuser:
		nivel = Inscripcion.objects.filter(id_nivel_id=3,estatus__range=["", "1"],terminado=False)
		paginator = Paginator(nivel, 7)
		page = request.GET.get("page", 1)
		try:
			nivel = paginator.page(page)
		except PageNotAnInteger:
			nivel = paginator.page(1)
		except EmptyPage:
			nivel = paginator.page(paginator.num_pages)
		buscador = request.GET

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
					return render(request,'aplicacion/nivel1_superuser.html', {"nivel":nivel})
		return render(request,'aplicacion/nivel1_superuser.html', {"nivel":nivel})
	else:
		return redirect('dato:app_inicio')


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
def retiro(request,pk):
	if request.method == 'POST':
		Inscripcion.objects.filter(cedula_id=pk).update(estatus=1,terminado=True)
		Users.objects.filter(pk=pk).update(is_active=False)
		return redirect('dato:app_inicio')
	return render(request,'aplicacion/retiro.html')


def post_new(request,*args, **kwargs):
	cedula = kwargs['pk']
	print (cedula)
	if request.user.is_profesor:
		filtro = Asigna_Materia.objects.get(profesor_id=request.user.ci)
		var = filtro.materia_id
		filtro2 = Materia.objects.get(id_materia=var)
		var2= filtro2.id_nivel_id
		print (var2)
		#print (var)
		nivel = Inscripcion.objects.get(id_nivel_id=var2,cedula_id=cedula)
		if nivel:
			print ('djksdns')
		else:
			print ('error')


		#print(nivel)
		filtro1  = Persona.objects.filter(cedula=cedula)
		#print (filtro1)
		nota = Notas.objects.filter(id_materia_id=var,cedula_id=nivel.id)
		calculo = Notas.objects.filter(cedula_id=nivel.id).aggregate(total=Sum('nota_persona'))
		#print (nota)
		nota_total = Notas.objects.filter(cedula_id=nivel.id)
		carga_total = len(nota_total)
		nota3 = len(nota)
		nota4 = nota3 + 1
		if nota3 != 0:
			for p in calculo.items():
				cantidad = (int(p[1]))
			print ('Nota total', cantidad)
			if cantidad >= 17 and carga_total >= 18 :
				Inscripcion.objects.filter(cedula_id=cedula).update(estatus=0)
			elif cantidad <17 and carga_total > 17 :
				Inscripcion.objects.filter(cedula_id=cedula).update(estatus=1)
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
		return render(request, 'aplicacion/nota_form.html', {'var2':var2,'nivel':nivel, 'nota4':nota4,'filtro1':filtro1,'nota3':nota3,'form':form,'cedula':cedula,'filtro':filtro})
	else:
		return redirect('dato:app_inicio')

class updateNota(UpdateView):
	model = Notas
	form_class = NotasUpdateForm
	template_name = 'aplicacion/nota_form1.html'
	success_url = reverse_lazy('dato:nivel1')

def solicitud(request):
	if request.user.is_alumno and not request.user.is_superuser:
		if request.method == 'POST':
			cedula = request.user.ci
			noto = {
				'titulo': 'Retiro',
				'descripcion': 'Deseo retirarme de la EDF.',
				'estatus': False,
				'user': cedula,}
			notificaciones =NotificacionesForm(noto)
			print (noto)
			notificaciones.save()
			#print (notificaciones)
			return redirect('dato:app_inicio')
		return render(request, 'aplicacion/form_solicitud.html')
	else:
		return redirect('dato:app_inicio')

class SolicitudCreate(CreateView):
	model = Persona
	template_name = 'aplicacion/aplicacion_form1.html'
	form_class = PersonaForm
	success_url = reverse_lazy('accounts:succesfull')


	def get_context_data(self, **kwargs):
		context = super(SolicitudCreate, self).get_context_data(**kwargs)
		if 'form' not in context:
			context['form'] = self.form_class(self.request.GET)
		return context

	def post(self, request, *args, **kwargs):
		self.object = self.get_object
		cedula = (request.POST['cedula'])
		print (cedula)
		form = self.form_class(request.POST)
		if form.is_valid():
			Users.objects.filter(ci=cedula).update(is_inscripcion=False)
			form.save()
			inscripcion = {
					'cedula': cedula,
					'id_nivel': 1,
					'estatus':1,
				}
			inscripciones =InscripcionForm(inscripcion)
			inscripciones.save()

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


def UsersCreateView_profesor(request,*args, **kwargs):
	if request.method == 'POST':
		form = UsersModelForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('dato:app_inicio')
	else:
		form = UsersModelForm()
	return render(request, 'aplicacion/form_create_profesor.html', {'form':form})

class ListProfesor(ListView):
	model = Profesor
	template_name = 'aplicacion/listprofesor.html'

class generar_pdf(View):
	def _header_footer(self,canvas,doc):
		canvas.saveState()
		canvas.setTitle("PDF")
		styles = getSampleStyleSheet()
		archivo_imagen = 'static/assets/img/gif.gif'
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
		    allclientes = [(len(p),p.ci,p.first_name, p.last_name, p.email) for p in Users.objects.all()]
		    t = Table([headings] + allclientes)
		    t.setStyle(TableStyle(
		    	[	('GRID', (0, 0), (7, -1), 1, colors.black),
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

class nivel1_pdf(View):
	def _header_footer(self,canvas,doc):
		canvas.saveState()
		canvas.setTitle("PDF")
		styles = getSampleStyleSheet()
		archivo_imagen = 'static/assets/img/gif.gif'
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
		header20 = Paragraph('Fecha: '+ time.strftime("%x"), styles['Normal'])
		w, h = header20.wrap(doc.width-320, doc.topMargin)
		header20.drawOn(canvas, 520, doc.height + doc.topMargin+15 )

		title = Paragraph('Lista de alumnos inscritos en el nivel 1', styles['Heading2'])
		w, h = title.wrap(doc.width-120, doc.topMargin)
		title.drawOn(canvas, 180, doc.height + doc.topMargin - 90)

		title1 = Paragraph('Alumnos:', styles['Heading4'])
		w, h = title1.wrap(doc.width-120, doc.topMargin)
		title1.drawOn(canvas, 280, doc.height + doc.topMargin - 160)

		header.drawOn(canvas, 250, doc.height + doc.topMargin - 41)
		footer = Paragraph('Iglesia Cristiana Bet-el Internacional', styles['Normal'])
		w, h = footer.wrap(doc.width, doc.bottomMargin)
		footer.drawOn(canvas, doc.leftMargin, h)
		canvas.restoreState()

	def get(self,request):
		print ("Genero el PDF")
		response = HttpResponse(content_type='application/pdf')
		pdf_name = "clientes.pdf"  # llamado clientes
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
			materias = Materia.objects.filter(id_nivel_id=1)
			id_materia1 = materias[0]
			id_materia2 = materias[1]
			obtener_id1 = id_materia1.id_materia
			obtener_id2 = id_materia2.id_materia
			nombre_pro = Asigna_Materia.objects.get(materia_id=obtener_id1)
			nombre1 = nombre_pro.profesor.nombre_profesor
			apellido1 = nombre_pro.profesor.apellido_profesor
			materia1 = id_materia1.nombre_materia
			nombre_completo = 'Profesor: '+nombre1+ ' '+apellido1+ ', Materia: '+materia1 
			print(nombre_completo)

			nombre_pro1 = Asigna_Materia.objects.get(materia_id=obtener_id2)
			nombre2 = nombre_pro1.profesor.nombre_profesor
			apellido2 = nombre_pro1.profesor.apellido_profesor
			materia2 = id_materia2.nombre_materia
			nombre_completo2 = 'Profesor: '+nombre2+ ' '+apellido2+ ', Materia: '+materia2 
			nombre_profesor1=Paragraph(nombre_completo,styles['Heading4'])
			header4=Paragraph('',styles['Heading3'])
			clientes.append(header4)
			clientes.append(header4)
			clientes.append(header4)
			clientes.append(header4)



			clientes.append(nombre_profesor1)
			nombre_profesor=Paragraph(nombre_completo2,styles['Heading4'])
			clientes.append(nombre_profesor)
			
			header4=Paragraph('',styles['Heading3'])
			clientes.append(header4)
			clientes.append(header4)
			clientes.append(header4)

			print(nombre_completo2)
			headings = ('N°','Cedula','Nombre', 'Apellido','Correo', 'Estatus')
			acum = 0
			lista = []
			for p in Inscripcion.objects.filter(id_nivel_id=1,terminado=False).order_by('cedula_id'):
				acum = acum+1
				if p.estatus=='1':
					estatus='Aprobado'
				else:
					estatus='Reprobado'
				print ('estatus ',estatus)
				var12 = (acum,p.cedula_id,p.cedula.nombre, p.cedula.apellido,p.cedula.email,estatus)
				lista.append(var12)
			t = Table([headings] + lista)
			t.setStyle(TableStyle(
		    	[	('GRID', (0, 0), (7, -1), 1, colors.black),
		    	('LINEBELOW', (0, 0), (-1, 0), 2, colors.black),
		    	('BACKGROUND', (0, 0), (-1, 0), colors.dodgerblue)
		    	]))
			clientes.append(t)
			header4=Paragraph('',styles['Heading3'])
			clientes.append(header4)
			cantidad = 'Cantidad de alumnos inscritos: '+str((len(lista)))

			header4=Paragraph(cantidad,styles['Normal'])
			clientes.append(header4)

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

class nivel2_pdf(View):
	def _header_footer(self,canvas,doc):
		canvas.saveState()
		canvas.setTitle("PDF")
		styles = getSampleStyleSheet()
		archivo_imagen = 'static/assets/img/gif.gif'
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
			header=Paragraph('Lista de Alumnos del nivel II',styles['Heading1'])
			clientes.append(header)
			materias = Materia.objects.filter(id_nivel_id=2)
			id_materia1 = materias[0]
			id_materia2 = materias[1]
			obtener_id1 = id_materia1.id_materia
			obtener_id2 = id_materia2.id_materia
			nombre_pro = Asigna_Materia.objects.get(materia_id=obtener_id1)
			nombre1 = nombre_pro.profesor.nombre_profesor
			apellido1 = nombre_pro.profesor.apellido_profesor
			materia1 = id_materia1.nombre_materia
			nombre_completo = 'Profesor: '+nombre1+ ' '+apellido1+ ' Materia: '+materia1 
			print(nombre_completo)

			nombre_pro1 = Asigna_Materia.objects.get(materia_id=obtener_id2)
			nombre2 = nombre_pro1.profesor.nombre_profesor
			apellido2 = nombre_pro1.profesor.apellido_profesor
			materia2 = id_materia2.nombre_materia
			nombre_completo2 = 'Profesor: '+nombre2+ ' '+apellido2+ ' Materia: '+materia2 
			nombre_profesor1=Paragraph(nombre_completo,styles['Heading4'])
			clientes.append(nombre_profesor1)
			nombre_profesor=Paragraph(nombre_completo2,styles['Heading4'])
			clientes.append(nombre_profesor)
			header1=Paragraph('ALumnos:',styles['Heading3'])

			clientes.append(header1)
			header4=Paragraph('',styles['Heading3'])
			clientes.append(header4)
			print(nombre_completo2)
			headings = ('Cedula','Nombre', 'Apellido','Correo', 'Estatus')
			allclientes = [(p.cedula_id,p.cedula.nombre, p.cedula.apellido,p.cedula.email,p.estatus) for p in Inscripcion.objects.filter(id_nivel_id=2,terminado=False)]
			
			t = Table([headings] + allclientes)
			t.setStyle(TableStyle(
		    	[	('GRID', (0, 0), (7, -1), 1, colors.black),
		    	('LINEBELOW', (0, 0), (-1, 0), 2, colors.black),
		    	('BACKGROUND', (0, 0), (-1, 0), colors.dodgerblue)
		    	]))
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

class nivel3_pdf(View):
	def _header_footer(self,canvas,doc):
		canvas.saveState()
		canvas.setTitle("PDF")
		styles = getSampleStyleSheet()
		archivo_imagen = 'static/assets/img/gif.gif'
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
			header=Paragraph('Lista de Alumnos del nivel III',styles['Heading1'])
			clientes.append(header)
			materias = Materia.objects.filter(id_nivel_id=3)
			id_materia1 = materias[0]
			id_materia2 = materias[1]
			obtener_id1 = id_materia1.id_materia
			obtener_id2 = id_materia2.id_materia
			nombre_pro = Asigna_Materia.objects.get(materia_id=obtener_id1)
			nombre1 = nombre_pro.profesor.nombre_profesor
			apellido1 = nombre_pro.profesor.apellido_profesor
			materia1 = id_materia1.nombre_materia
			nombre_completo = 'Profesor: '+nombre1+ ' '+apellido1+ ' Materia: '+materia1 
			print(nombre_completo)

			nombre_pro1 = Asigna_Materia.objects.get(materia_id=obtener_id2)
			nombre2 = nombre_pro1.profesor.nombre_profesor
			apellido2 = nombre_pro1.profesor.apellido_profesor
			materia2 = id_materia2.nombre_materia
			nombre_completo2 = 'Profesor: '+nombre2+ ' '+apellido2+ ' Materia: '+materia2 
			nombre_profesor1=Paragraph(nombre_completo,styles['Heading4'])
			clientes.append(nombre_profesor1)
			nombre_profesor=Paragraph(nombre_completo2,styles['Heading4'])
			clientes.append(nombre_profesor)
			header1=Paragraph('ALumnos:',styles['Heading3'])

			clientes.append(header1)
			header4=Paragraph('',styles['Heading3'])
			clientes.append(header4)
			print(nombre_completo2)
			headings = ('Cedula','Nombre', 'Apellido','Correo', 'Estatus')
			allclientes = [(p.cedula_id,p.cedula.nombre, p.cedula.apellido,p.cedula.email,p.estatus) for p in Inscripcion.objects.filter(id_nivel_id=3,terminado=False)]
			
			t = Table([headings] + allclientes)
			t.setStyle(TableStyle(
		    	[	('GRID', (0, 0), (7, -1), 1, colors.black),
		    	('LINEBELOW', (0, 0), (-1, 0), 2, colors.black),
		    	('BACKGROUND', (0, 0), (-1, 0), colors.dodgerblue)
		    	]))
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
		canvas.setTitle("PDF")
		styles = getSampleStyleSheet()
		archivo_imagen = 'static/assets/img/gif.gif'
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
		    headings3 = ('Iglesia   ','Pastor    ', 'Estudio Teologico             ', 'Instituto                      ','Titulo Obtenido                                ')
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