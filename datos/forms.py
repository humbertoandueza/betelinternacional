from django.db import models
from django.forms import ModelForm
from django import forms
from .models import *

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class PersonaForm(forms.ModelForm):

	class Meta:
		model = Persona
		fields= [
			'cedula',
			'nombre',
			'apellido',
			'fecha_de_nacimiento',
			'sexo',
			'direccion',
			'telefono_residencial',
			'celular_number',
			'celular',
			'email',
			'estado_civil',
			'trabaja',
			'profesion',
			'estudio_ori',
			'ing_famil',
			'iglesia',
			'pastor',
			'estudio_teo',
			'instituto',
			'titulo_obte',
			'actividad',
			'ministerio',
			'razon',
			'user',

		]
		widgets = {
            'user': forms.NumberInput(attrs={'readonly':'readonly','value':'27277934','placeholder': 'Cedula', 'class':'form-control', 'autocomplete':'off','oninput':'maxLengthCheck(this)','maxlength':'8','onKeyUp':'this.value=this.value.toUpperCase();'}),
			#'user': forms.Select(attrs={'class':'form-control', 'autocomplete':'off'}),		
            'cedula': forms.NumberInput(attrs={'placeholder': 'Cedula', 'class':'form-control', 'autocomplete':'off','oninput':'maxLengthCheck(this)','maxlength':'8','onKeyUp':'this.value=this.value.toUpperCase();'}),
            'nombre': forms.TextInput(attrs={'placeholder': 'Nombre', 'class':'form-control', 'autocomplete':'off','onkeypress':'return text(event)','onKeyUp':'this.value=this.value.toUpperCase();'}),
            'apellido': forms.TextInput(attrs={'placeholder': 'Apellido', 'class':'form-control', 'autocomplete':'off','onkeypress':'return text(event)','onKeyUp':'this.value=this.value.toUpperCase();'}),
            
            'fecha_de_nacimiento': forms.DateInput(attrs={'placeholder': '1999-09-09', 'class':'form-control','type':'date'}),
            'sexo': forms.Select(attrs={'class':'form-control', 'autocomplete':'off'}),
            'direccion': forms.TextInput(attrs={'placeholder': 'Direccion', 'class':'form-control', 'autocomplete':'off','onKeyUp':'this.value=this.value.toUpperCase();'}),
            'telefono_residencial': forms.TextInput(attrs={'placeholder': 'Numero Residencial', 'class':'form-control bfh-phone', 'autocomplete':'off','oninput':'maxLengthCheck(this)','data-format':'dddd-ddd-dddd'}),
            'celular_number': forms.TextInput(attrs={'placeholder': 'Numero Celular', 'class':'form-control bfh-phone', 'autocomplete':'off','oninput':'maxLengthCheck(this)','data-format':'ddd-dddd'}),
            'celular': forms.Select(attrs={'class':'form-control', 'autocomplete':'off','onKeyUp':'this.value=this.value.toUpperCase();'}),
            
            'email': forms.EmailInput(attrs={ 'placeholder': 'Email', 'class':'form-control', 'autocomplete':'off','onKeyUp':'this.value=this.value.toUpperCase();'}),
			
			'estado_civil': forms.Select(attrs={'class':'form-control', 'autocomplete':'off','onKeyUp':'this.value=this.value.toUpperCase();'}),
			'trabaja': forms.Select(attrs={'class':'form-control', 'autocomplete':'off','onKeyUp':'this.value=this.value.toUpperCase();'}),
			'profesion': forms.TextInput(attrs={'placeholder':'Profesion','class':'form-control', 'autocomplete':'off','onkeypress':'return text(event)','onKeyUp':'this.value=this.value.toUpperCase();'}),
			'estudio_ori':forms.TextInput(attrs={'placeholder':'Origen de Estudio','class':'form-control', 'autocomplete':'off','onkeypress':'return text(event)','onKeyUp':'this.value=this.value.toUpperCase();'}),
			'ing_famil':forms.NumberInput(attrs={'placeholder':'Ingreso Familiar','class':'form-control', 'autocomplete':'off','onKeyUp':'this.value=this.value.toUpperCase();'}),
			'iglesia':forms.TextInput(attrs={'placeholder':'Iglesia a la que Asiste','class':'form-control', 'autocomplete':'off','onkeypress':'return text(event)','onKeyUp':'this.value=this.value.toUpperCase();'}),
			'pastor':forms.TextInput(attrs={'placeholder':'Pastor de Congregacion','class':'form-control', 'autocomplete':'off','onkeypress':'return text(event)','onKeyUp':'this.value=this.value.toUpperCase();'}),
			'estudio_teo':forms.Select(attrs={'class':'form-control ', 'autocomplete':'off','onkeypress':'return text(event)','onKeyUp':'this.value=this.value.toUpperCase();','onchange':'showDiv(this)'}),
			'instituto':forms.TextInput(attrs={'placeholder':'Instituto de Estudio','class':'form-control', 'autocomplete':'off','onKeyUp':'this.value=this.value.toUpperCase();'}),
			'titulo_obte':forms.TextInput(attrs={'placeholder':'Titulo Obtenido','class':'form-control', 'autocomplete':'off','onkeypress':'return text(event)','onKeyUp':'this.value=this.value.toUpperCase();'}),
			'actividad':forms.TextInput(attrs={'placeholder':'Actividad que realiza en la Iglesia','class':'form-control', 'autocomplete':'off','onkeypress':'return text(event)','onKeyUp':'this.value=this.value.toUpperCase();'}),
			'ministerio':forms.Select(attrs={'class':'form-control', 'autocomplete':'off'}),
			'razon':forms.TextInput(attrs={'placeholder':'Razon por la cual desea estudiar ','class':'form-control', 'autocomplete':'off','onkeypress':'return text(event)','onKeyUp':'this.value=this.value.toUpperCase();'}), 
    		
    		}

class NivelForm(forms.ModelForm):

	class Meta:
		model = Nivel
		fields= [
			'nivel'
		]
		widgets = {
            'nivel': forms.TextInput(attrs={'placeholder': 'Nivel', 'class':'form-control', 'autocomplete':'off', 'onKeyUp':'this.value=this.value.toUpperCase();','onkeypress':'return texto(event)'}),
		}

class InscripcionForm(forms.ModelForm):

	class Meta:
		model = Inscripcion
		fields= [
			'cedula',
			'id_nivel',
			'estatus',
		]
		widgets = {
            'cedula': forms.NumberInput(attrs={'placeholder': 'Cedula', 'class':'form-control', 'autocomplete':'off','oninput':'maxLengthCheck(this)','maxlength':'8','onKeyUp':'this.value=this.value.toUpperCase();'}),
			
			#'id_nivel': forms.TextInput(attrs={'value':'1','class':'form-control','readonly':'readonly'}),
		}

class ProfesorForm(forms.ModelForm):

	class Meta:
		model = Profesor
		fields= [
			'cedula_profesor',
			'nombre_profesor',
			'apellido_profesor',
			'telefono_profesor',
			'email_profesor',
			'user',
			'estatus',
		]
		widgets = {
            'cedula_profesor': forms.NumberInput(attrs={'placeholder': 'Cedula', 'class':'form-control', 'autocomplete':'off','oninput':'maxLengthCheck(this)','maxlength':'8','onKeyUp':'this.value=this.value.toUpperCase();'}),
            'nombre_profesor': forms.TextInput(attrs={'placeholder': 'Nombre', 'class':'form-control', 'autocomplete':'off','onkeypress':'return text(event)','onKeyUp':'this.value=this.value.toUpperCase();'}),
            'apellido_profesor': forms.TextInput(attrs={'placeholder': 'Apellido', 'class':'form-control', 'autocomplete':'off','onkeypress':'return text(event)','onKeyUp':'this.value=this.value.toUpperCase();'}),
            'telefono_profesor': forms.TextInput(attrs={'placeholder': 'Numero Celular', 'class':'form-control', 'autocomplete':'off','oninput':'maxLengthCheck(this)','min':'1','max':'9999999999','maxlength':'11'}),
            'email_profesor': forms.EmailInput(attrs={'placeholder': 'Email', 'class':'form-control', 'autocomplete':'off','onKeyUp':'this.value=this.value.toUpperCase();'}),
            'user': forms.NumberInput(attrs={'placeholder': 'Cedula', 'class':'form-control', 'autocomplete':'off','oninput':'maxLengthCheck(this)','maxlength':'8','onKeyUp':'this.value=this.value.toUpperCase();'}),
            'estatus': forms.CheckboxInput(attrs={'checked':'checked'}),
			
		}

class MateriaForm(forms.ModelForm):

	class Meta:
		model = Materia
		fields= [
			'nombre_materia',
			'id_nivel',
		]
		widgets = {
            'nombre_materia': forms.TextInput(attrs={'placeholder': 'Nombre', 'class':'form-control', 'autocomplete':'off','onkeypress':'return text(event)','onKeyUp':'this.value=this.value.toUpperCase();'}),
			'id_nivel': forms.Select(attrs={'class':'form-control', 'autocomplete':'off','onKeyUp':'this.value=this.value.toUpperCase();'}),
            
		}


class AsignaMateriaForm(forms.ModelForm):

	class Meta:
		model = Asigna_Materia
		fields= [
			'materia',
			'profesor',
		]
		widgets = {
			'profesor': forms.Select(attrs={'class':'form-control', 'autocomplete':'off','onKeyUp':'this.value=this.value.toUpperCase();'}),
			'materia': forms.Select(attrs={'class':'form-control', 'autocomplete':'off','onKeyUp':'this.value=this.value.toUpperCase();'}),
            
		}


class NotasForm(forms.ModelForm):

	class Meta:
		model = Notas
		fields= [
			'cedula',
			'id_materia',
			'nota_persona'
		]
		widgets = {
            'cedula': forms.NumberInput(attrs={'placeholder': 'Cedula', 'class':'form-control', 'autocomplete':'off','oninput':'maxLengthCheck(this)','maxlength':'8','onKeyUp':'this.value=this.value.toUpperCase();'}),
			'id_materia': forms.Select(attrs={'class':'form-control', 'autocomplete':'off','onKeyUp':'this.value=this.value.toUpperCase();'}),
			'nota_persona': forms.Select(attrs={'class':'form-control', 'autocomplete':'off','onKeyUp':'this.value=this.value.toUpperCase();'}),            
		}

class NotificacionesForm(forms.ModelForm):

	class Meta:
		model = Notificacion
		fields= [
			'titulo',
			'descripcion',
			'estatus',
			'user'
		]