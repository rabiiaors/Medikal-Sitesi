# Generated by Django 4.2 on 2023-05-29 19:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Setting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('keywords', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=255)),
                ('company', models.CharField(max_length=50)),
                ('address', models.CharField(blank=True, max_length=100)),
                ('phone', models.CharField(blank=True, max_length=255)),
                ('fax', models.CharField(blank=True, max_length=15)),
                ('email', models.CharField(blank=True, max_length=50)),
                ('smtpserver', models.CharField(max_length=50)),
                ('smtpemail', models.CharField(max_length=50)),
                ('smtppassword', models.CharField(max_length=10)),
                ('smtpport', models.CharField(blank=True, max_length=50)),
                ('icon', models.ImageField(blank=True, upload_to='images/')),
                ('facebook', models.CharField(max_length=50)),
                ('instagram', models.CharField(max_length=50)),
                ('twitter', models.CharField(max_length=50)),
                ('aboutus', models.CharField(max_length=50)),
                ('references', models.CharField(max_length=50)),
                ('status', models.CharField(choices=[('True', 'True'), ('False', 'False')], max_length=10)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
