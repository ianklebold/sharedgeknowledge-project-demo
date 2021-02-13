# Generated by Django 3.1.5 on 2021-01-26 01:36

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
            name='Categoria',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100, verbose_name='Nombre de categoria')),
                ('fecha_creacion', models.DateField(auto_now_add=True, verbose_name='Fecha de creación')),
            ],
            options={
                'verbose_name': 'Categoria',
                'verbose_name_plural': 'Categorias',
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('titulo', models.CharField(max_length=90, verbose_name='Titulo')),
                ('texto', models.CharField(blank=True, max_length=280, null=True, verbose_name='Descripcion')),
                ('video', models.URLField(blank=True, max_length=400, null=True, verbose_name='Enlace de Youtube')),
                ('enlace_web', models.URLField(blank=True, max_length=400, null=True, verbose_name='Enlace web')),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='imagenes/')),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creacion')),
                ('archivo', models.FileField(upload_to='documentos/')),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Create_Post.categoria')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='posts', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Post',
                'verbose_name_plural': 'Posts',
                'ordering': ['-fecha_creacion'],
            },
        ),
    ]