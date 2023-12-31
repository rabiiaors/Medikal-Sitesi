# Generated by Django 4.2 on 2023-05-29 21:24

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_images'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='slug',
            field=models.SlugField(blank=True, max_length=150),
        ),
        migrations.AlterField(
            model_name='product',
            name='detail',
            field=ckeditor_uploader.fields.RichTextUploadingField(),
        ),
    ]
