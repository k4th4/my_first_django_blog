# Generated by Django 3.2.21 on 2023-10-12 14:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('squint', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sqimage',
            name='image_path',
        ),
    ]