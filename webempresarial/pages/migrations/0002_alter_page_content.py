# Generated by Django 4.1.3 on 2022-11-15 21:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='content',
            field=models.TextField(verbose_name='Contenido'),
        ),
    ]
