# Generated by Django 4.1 on 2022-08-16 06:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0002_auto_20220814_1338'),
    ]

    operations = [
        migrations.CreateModel(
            name='TaskComment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tittle', models.CharField(max_length=100)),
                ('hora', models.CharField(blank=True, max_length=100, null=True)),
                ('fecha', models.DateField(blank=True, null=True, verbose_name='%A, %B %d, %Y %H:%M:%S')),
                ('description', models.TextField(blank=True)),
            ],
        ),
    ]
