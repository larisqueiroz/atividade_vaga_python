# Generated by Django 4.0.4 on 2022-05-10 20:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='objeto',
            name='objeto_tipo_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='app.objeto_tipo'),
        ),
    ]
