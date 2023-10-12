# Generated by Django 3.2.21 on 2023-10-12 14:12

from django.db import migrations, models
import squint.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SqImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_grey', models.BooleanField(default=True)),
                ('image_path', models.FilePathField(path=squint.models.images_path)),
                ('notan_levels', models.IntegerField(choices=[(2, 'two'), (3, 'three'), (4, 'four')], default=2)),
                ('posterize_level', models.IntegerField(default=3)),
                ('blur_level', models.IntegerField(default=7)),
                ('output_file_format', models.CharField(default='.png', max_length=200)),
            ],
        ),
    ]
