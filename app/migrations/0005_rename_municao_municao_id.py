# Generated by Django 4.0.4 on 2022-05-13 19:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_rename_objeto_tipo_id_objeto_objeto_tipo'),
    ]

    operations = [
        migrations.RenameField(
            model_name='municao',
            old_name='municao',
            new_name='id',
        ),
    ]