# Generated by Django 4.0.5 on 2022-07-04 23:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lines_count', models.IntegerField(null=True)),
                ('file_size', models.IntegerField(null=True)),
                ('file_url', models.CharField(max_length=120)),
                ('status', models.IntegerField(choices=[(0, 'Pending'), (1, 'Processing'), (2, 'Processed'), (3, 'Failed')], default=0)),
            ],
        ),
    ]
