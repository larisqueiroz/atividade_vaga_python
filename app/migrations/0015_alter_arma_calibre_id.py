# Generated by Django 4.0.4 on 2022-05-12 17:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0014_alter_arma_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='arma',
            name='calibre_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='app.calibre'),
        ),
    ]
