# Generated by Django 2.2.13 on 2022-05-08 17:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comida',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
                ('descripcion', models.TextField()),
                ('precio', models.CharField(max_length=20)),
                ('imagen', models.ImageField(upload_to='establecimientos/platillo')),
            ],
        ),
        migrations.CreateModel(
            name='Establecimientos',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
                ('ciudad', models.CharField(max_length=40)),
                ('departamento', models.CharField(max_length=40)),
                ('rango_precios', models.CharField(max_length=50)),
                ('parqueadero', models.BooleanField()),
                ('correo', models.EmailField(max_length=254)),
                ('tarjeta_credito', models.BooleanField()),
                ('tarjetas_debito', models.BooleanField()),
                ('descripcion', models.TextField()),
                ('tipo', models.CharField(choices=[('Restaurante', 'Restaurante'), ('Cafeteria', 'Cafeteria'), ('Bar', 'Bar'), ('CafeBar', 'CafeBar')], default='Restaurante', max_length=20)),
                ('direccion', models.CharField(max_length=50)),
                ('imagen', models.ImageField(upload_to='establecimientos/foto-principal')),
                ('imagen_banner', models.ImageField(upload_to='establecimientos/banner')),
                ('slug', models.SlugField(blank=True, max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.SlugField(blank=True, max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Servicios',
            fields=[
                ('nombre', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('fin_semana', models.BooleanField()),
            ],
        ),
        migrations.RemoveField(
            model_name='categorias',
            name='idCategoria',
        ),
        migrations.RemoveField(
            model_name='users',
            name='id',
        ),
        migrations.AlterField(
            model_name='categorias',
            name='nombre',
            field=models.CharField(max_length=50, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='contacto',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='users',
            name='nombreUsuario',
            field=models.CharField(max_length=250, primary_key=True, serialize=False),
        ),
        migrations.DeleteModel(
            name='Productos',
        ),
        migrations.AddField(
            model_name='establecimientos',
            name='categoria',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='myapp.Categorias'),
        ),
        migrations.AddField(
            model_name='establecimientos',
            name='menu',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='myapp.Menu'),
        ),
        migrations.AddField(
            model_name='establecimientos',
            name='servicios',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='myapp.Servicios'),
        ),
    ]
