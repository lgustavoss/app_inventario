# Generated by Django 4.0.6 on 2022-07-24 18:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('colaborador', '0002_colaborador_status'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='colaborador',
            options={'ordering': ['nome']},
        ),
    ]
