# Generated by Django 4.1.6 on 2023-02-07 22:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App1', '0004_ayudante_duenio'),
    ]

    operations = [
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=40)),
                ('camada', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Estudiante',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=40)),
                ('apellido', models.CharField(max_length=40)),
                ('correo', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Profesor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=40)),
                ('apellido', models.CharField(max_length=40)),
                ('email', models.EmailField(max_length=254)),
                ('profesion', models.CharField(max_length=60)),
            ],
        ),
        migrations.DeleteModel(
            name='Ayudante',
        ),
        migrations.DeleteModel(
            name='Duenio',
        ),
        migrations.DeleteModel(
            name='Empleado',
        ),
    ]