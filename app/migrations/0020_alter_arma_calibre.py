# Generated by Django 4.0.4 on 2022-05-12 21:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0019_alter_arma_arma'),
    ]

    operations = [
        migrations.AlterField(
            model_name='arma',
            name='calibre',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.calibre'),
        ),
    ]
