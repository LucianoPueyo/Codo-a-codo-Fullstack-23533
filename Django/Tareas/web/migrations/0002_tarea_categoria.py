# Generated by Django 4.2.7 on 2023-11-29 14:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tarea',
            name='categoria',
            field=models.CharField(max_length=100, null=True, verbose_name='Categoria'),
        ),
    ]