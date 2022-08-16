# Generated by Django 4.1 on 2022-08-13 17:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Titulo', models.CharField(max_length=100)),
                ('Fecha', models.CharField(max_length=100)),
                ('NombreDeAutor', models.CharField(max_length=100)),
                ('Cuerpo', models.CharField(max_length=100)),
                ('Imagen', models.ImageField(null=True, upload_to='imagenes/', verbose_name='Imagen')),
            ],
        ),
    ]