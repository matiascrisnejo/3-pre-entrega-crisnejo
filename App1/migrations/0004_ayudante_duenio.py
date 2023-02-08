# Generated by Django 4.1.6 on 2023-02-07 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App1', '0003_delete_ayudante_delete_duenio'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ayudante',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=40)),
                ('apellido', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Duenio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=40)),
                ('apellido', models.CharField(max_length=40)),
            ],
        ),
    ]
