# Generated by Django 4.0.5 on 2022-07-14 23:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('file', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='file',
            old_name='file_url',
            new_name='file_path',
        ),
    ]