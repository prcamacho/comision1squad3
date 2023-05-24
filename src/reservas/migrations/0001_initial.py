# Generated by Django 4.2.1 on 2023-05-23 10:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('clientes', '0001_initial'),
        ('coordinador', '0002_alter_coordinador_fecha_alta'),
        ('empleados', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReservaServicio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('fecha_reserva', models.DateTimeField()),
                ('precio', models.DecimalField(decimal_places=2, max_digits=10)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='clientes.cliente')),
                ('empleado', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='empleados.empleado')),
                ('responsable', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='coordinador.coordinador')),
            ],
        ),
    ]
