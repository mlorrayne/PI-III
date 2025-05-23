# Generated by Django 5.2.1 on 2025-05-24 21:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_gasto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gasto',
            name='item',
            field=models.CharField(choices=[('Aluguel', 'Aluguel'), ('Cestas Básicas', 'Cestas Básicas'), ('Transporte', 'Transporte'), ('Eventos', 'Eventos')], max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='gasto',
            name='valor',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
    ]
