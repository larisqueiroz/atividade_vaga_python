# Generated by Django 4.0.4 on 2022-05-12 21:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0018_rename_id_arma_arma_rename_calibre_id_arma_calibre'),
    ]

    operations = [
        migrations.AlterField(
            model_name='arma',
            name='arma',
            field=models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='app.objeto'),
        ),
    ]
