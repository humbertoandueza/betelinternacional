# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-03-13 19:19
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Asigna_Materia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Inscripcion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lapso_ano', models.DateField(auto_now_add=True)),
                ('estatus', models.CharField(blank=True, choices=[('0', 'Aprobado'), ('1', 'Reprobado')], max_length=20)),
                ('terminado', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Materia',
            fields=[
                ('id_materia', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_materia', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Nivel',
            fields=[
                ('id_nivel', models.AutoField(primary_key=True, serialize=False)),
                ('nivel', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Notas',
            fields=[
                ('id_nota', models.AutoField(primary_key=True, serialize=False)),
                ('nota_persona', models.CharField(choices=[('', 'Nota'), ('1', 'Aprobado'), ('0', 'Reprobado')], max_length=20)),
                ('cedula', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='datos.Inscripcion')),
                ('id_materia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='datos.Materia')),
            ],
        ),
        migrations.CreateModel(
            name='Notificacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=20)),
                ('descripcion', models.CharField(max_length=80)),
                ('hora', models.DateTimeField(auto_now=True)),
                ('estatus', models.NullBooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('cedula', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=60)),
                ('apellido', models.CharField(max_length=60)),
                ('fecha_de_nacimiento', models.DateField()),
                ('sexo', models.CharField(choices=[('', 'Sexo'), ('Femenino', 'Femenino'), ('Masculino', 'Masculino')], max_length=15)),
                ('direccion', models.CharField(max_length=60)),
                ('telefono_residencial', models.CharField(blank=True, max_length=14)),
                ('celular_number', models.CharField(blank=True, max_length=20)),
                ('celular', models.CharField(blank=True, choices=[('0424', '0424'), ('0414', '0414'), ('0426', '0426'), ('0416', '0416'), ('0412', '0412')], max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('estado_civil', models.CharField(choices=[('', 'Estado Civil'), ('Soltero', 'Soltero/a'), ('Casado', 'Casado/a'), ('Divorciado', 'Divorciado/a'), ('Viudo', 'Viudo/a')], max_length=15)),
                ('trabaja', models.CharField(choices=[('', 'Trabaja'), ('si', 'Si'), ('no', 'No')], max_length=10)),
                ('profesion', models.CharField(max_length=60)),
                ('estudio_ori', models.CharField(max_length=60)),
                ('ing_famil', models.CharField(max_length=60)),
                ('iglesia', models.CharField(max_length=60)),
                ('pastor', models.CharField(max_length=25)),
                ('estudio_teo', models.CharField(choices=[('', 'Estudio Teologia'), ('si', 'Si'), ('no', 'No')], max_length=20)),
                ('instituto', models.CharField(blank=True, max_length=60, null=True)),
                ('titulo_obte', models.CharField(blank=True, max_length=25, null=True)),
                ('actividad', models.CharField(max_length=60)),
                ('ministerio', models.CharField(choices=[('', 'Ministerio'), ('Adoracion', 'Adoracion y Alabanza'), ('Audiovisual', 'Audiovisual'), ('Intercesion', 'Intersecion'), ('Consolidacion', 'Consolidacion'), ('Liberacion', 'Liberacion y Restauracion'), ('Eduacion', 'Educacion Cristiana'), ('Protocolo', 'Protocolo y Servicio')], max_length=60)),
                ('razon', models.CharField(max_length=60)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Profesor',
            fields=[
                ('cedula_profesor', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre_profesor', models.CharField(max_length=20)),
                ('apellido_profesor', models.CharField(max_length=20)),
                ('telefono_profesor', models.CharField(max_length=11)),
                ('email_profesor', models.EmailField(max_length=254)),
                ('estatus', models.NullBooleanField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='notificacion',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='datos.Persona'),
        ),
        migrations.AddField(
            model_name='materia',
            name='id_nivel',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='datos.Nivel'),
        ),
        migrations.AddField(
            model_name='inscripcion',
            name='cedula',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='datos.Persona'),
        ),
        migrations.AddField(
            model_name='inscripcion',
            name='id_nivel',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='datos.Nivel'),
        ),
        migrations.AddField(
            model_name='asigna_materia',
            name='materia',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='datos.Materia'),
        ),
        migrations.AddField(
            model_name='asigna_materia',
            name='profesor',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='datos.Profesor'),
        ),
    ]