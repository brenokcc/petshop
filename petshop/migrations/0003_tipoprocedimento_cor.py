# Generated by Django 4.0.4 on 2022-05-14 14:50

from django.db import migrations
import sloth.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('petshop', '0002_administrador'),
    ]

    operations = [
        migrations.AddField(
            model_name='tipoprocedimento',
            name='cor',
            field=sloth.db.models.ColorField(default='#FFFFFF', max_length=7, verbose_name='Cor'),
        ),
    ]