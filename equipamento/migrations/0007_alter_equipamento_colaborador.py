# Generated by Django 4.0.6 on 2022-07-24 22:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('colaborador', '0003_alter_colaborador_options'),
        ('equipamento', '0006_alter_equipamento_marca_alter_equipamento_modelo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='equipamento',
            name='colaborador',
            field=models.ForeignKey(limit_choices_to={'status': True}, on_delete=django.db.models.deletion.PROTECT, to='colaborador.colaborador'),
        ),
    ]