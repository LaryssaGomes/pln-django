# Generated by Django 4.0.2 on 2022-02-01 20:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pnlPdf', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='palavra',
            name='FKArtigoId',
        ),
        migrations.RemoveField(
            model_name='sentenca',
            name='FkArtigoId',
        ),
        migrations.DeleteModel(
            name='Artigo',
        ),
        migrations.DeleteModel(
            name='Palavra',
        ),
        migrations.DeleteModel(
            name='Sentenca',
        ),
    ]
