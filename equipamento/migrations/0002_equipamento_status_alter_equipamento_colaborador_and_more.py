# Generated by Django 4.0.6 on 2022-07-16 00:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('empresa', '0002_empresa_status'),
        ('colaborador', '0002_colaborador_status'),
        ('tipo_equipamento', '0002_tipoequipamento_status'),
        ('equipamento', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='equipamento',
            name='status',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='equipamento',
            name='colaborador',
            field=models.ForeignKey(blank=True, limit_choices_to={'status': True}, null=True, on_delete=django.db.models.deletion.PROTECT, to='colaborador.colaborador'),
        ),
        migrations.AlterField(
            model_name='equipamento',
            name='empresa',
            field=models.ForeignKey(limit_choices_to={'status': True}, on_delete=django.db.models.deletion.PROTECT, to='empresa.empresa'),
        ),
        migrations.AlterField(
            model_name='equipamento',
            name='tipo_equipamento',
            field=models.ForeignKey(limit_choices_to={'status': True}, on_delete=django.db.models.deletion.PROTECT, to='tipo_equipamento.tipoequipamento'),
        ),
    ]
