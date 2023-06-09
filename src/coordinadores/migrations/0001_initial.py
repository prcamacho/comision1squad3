# Generated by Django 4.2.1 on 2023-06-03 06:20

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Coordinador',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('apellido', models.CharField(max_length=50)),
                ('numero_documento', models.PositiveBigIntegerField()),
                ('fecha_alta', models.DateTimeField(default=datetime.datetime(2023, 6, 3, 3, 20, 43, 292898))),
                ('activo', models.BooleanField(default=True)),
            ],
        ),
    ]
