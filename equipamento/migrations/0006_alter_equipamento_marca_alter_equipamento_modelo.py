# Generated by Django 4.0.6 on 2022-07-24 22:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('equipamento', '0005_alter_equipamento_marca'),
    ]

    operations = [
        migrations.AlterField(
            model_name='equipamento',
            name='marca',
            field=models.CharField(default='-', max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='equipamento',
            name='modelo',
            field=models.CharField(default='--', max_length=50),
            preserve_default=False,
        ),
    ]
