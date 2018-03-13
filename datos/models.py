from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from accounts.models import Users
# Create your models here.

class Persona(models.Model):
	cedula = models.IntegerField(primary_key=True)
	nombre = models.CharField(max_length=60)
	apellido = models.CharField(max_length=60)
	fecha_de_nacimiento = models.DateField()
	sexo1 = (
		('','Sexo'),
		('Femenino','Femenino'),
		('Masculino','Masculino'),
		)
	sexo= models.CharField(max_length=15,choices=sexo1)
	direccion = models.CharField(max_length=60)
	telefono_residencial = models.CharField(max_length=14,blank=True)
	codi_celular=(
		("0424","0424"),
		("0414","0414"),
		("0426","0426"),
		("0416","0416"),
		("0412","0412"),
	)
	celular_number = models.CharField(max_length=20,blank=True)
	celular=models.CharField(max_length=20,choices=codi_celular,blank=True)

	email = models.EmailField()
	estado = (
			('','Estado Civil'),
			('Soltero','Soltero/a'),
			('Casado','Casado/a'),
			('Divorciado','Divorciado/a'),
			('Viudo','Viudo/a')
		)
	estado_civil = models.CharField(max_length=15,choices=estado)
	tr = (
			('', 'Trabaja'),
			('si','Si'),
			('no', 'No'),
		)
	trabaja = models.CharField(max_length=10,choices=tr)
	profesion = models.CharField(max_length=60)
	estudio_ori = models.CharField(max_length=60)
	ing_famil = models.CharField(max_length=60)
	iglesia = models.CharField(max_length=60)
	pastor = models.CharField(max_length=25)
	es = (
			('','Estudio Teologia'),
			('si','Si'),
			('no','No')
			)
	estudio_teo = models.CharField(max_length=20,choices=es)
	instituto = models.CharField(max_length=60,null=True,blank=True)
	titulo_obte = models.CharField(max_length=25,null=True,blank=True)
	actividad = models.CharField(max_length=60)
	mini= (
			('', 'Ministerio'),
			('Adoracion', 'Adoracion y Alabanza'),
			('Audiovisual','Audiovisual'),
			('Intercesion','Intersecion'),
			('Consolidacion', 'Consolidacion'),
			('Liberacion', 'Liberacion y Restauracion'),
			('Eduacion', 'Educacion Cristiana'),
			('Protocolo','Protocolo y Servicio')
		)
	ministerio = models.CharField(max_length=60,choices=mini)
	razon = models.CharField(max_length=60)
	user = models.ForeignKey(Users)


	def __str__(self):
		return str(self.cedula)

class Nivel(models.Model):
	id_nivel = models.AutoField(primary_key=True)
	nivel = models.CharField(max_length=10)

	def __str__(self):
		return str(self.nivel)

class Profesor(models.Model):
	cedula_profesor = models.IntegerField(primary_key=True)
	nombre_profesor = models.CharField(max_length=20)
	apellido_profesor = models.CharField(max_length=20)
	telefono_profesor = models.CharField(max_length=11)
	email_profesor = models.EmailField()
	estatus = models.NullBooleanField()
	user = models.ForeignKey(Users)

	def __str__(self): #si es python 2.7 es def __unicode__(self):
		return '{}, {}' .format( self.nombre_profesor,self.cedula_profesor)

class  Materia(models.Model):
	id_materia = models.AutoField(primary_key=True)
	nombre_materia = models.CharField(max_length=40)
	id_nivel = models.ForeignKey(Nivel)

	def __str__(self): #si es python 2.7 es def __unicode__(self):
		return '{}, {}' .format(self.nombre_materia, self.id_nivel)


class Inscripcion(models.Model):
	cedula = models.ForeignKey(Persona)
	id_nivel = models.ForeignKey(Nivel)
	lapso_ano = models.DateField(auto_now_add=True)
	est=(
		("0","Aprobado"),
		("1","Reprobado"),

	)
	estatus = models.CharField(max_length=20,choices=est,blank=True)
	terminado = models.BooleanField(default=False)


	def __str__(self):
		return str(self.id)


class Asigna_Materia(models.Model):
	materia = models.OneToOneField(Materia)
	profesor = models.OneToOneField(Profesor)


	def __str__(self): #si es python 2.7 es def __unicode__(self):
		return '{}, {}' .format(self.materia, self.profesor)


class Notas(models.Model):
	id_nota = models.AutoField(primary_key=True)
	cedula = models.ForeignKey(Inscripcion)
	id_materia = models.ForeignKey(Materia)
	es = (
			('','Nota'),
			('1','Aprobado'),
			('0','Reprobado')
			)
	nota_persona = models.CharField(max_length=20,choices=es)

	def __str__(self):
		return self.nota_persona

class Notificacion(models.Model):
	titulo = models.CharField(max_length=20)
	descripcion = models.CharField(max_length=80)
	hora = models.DateTimeField(auto_now=True)
	user = models.ForeignKey(Persona)
	estatus = models.NullBooleanField()

	def __str__(self):
		return self.titulo

