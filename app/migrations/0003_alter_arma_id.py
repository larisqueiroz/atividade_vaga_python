# Generated by Django 4.0.4 on 2022-05-10 21:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_objeto_objeto_tipo_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='arma',
            name='id',
            field=models.ForeignKey(db_column='id', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='app.objeto'),
        ),
    ]