# Generated by Django 2.2.13 on 2022-05-12 01:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_alter_contacto_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contacto',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
