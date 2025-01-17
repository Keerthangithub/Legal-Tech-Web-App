# Generated by Django 4.2.1 on 2024-01-18 14:24

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_message'),
    ]

    operations = [
        migrations.CreateModel(
            name='Fileupload',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='uploaded_files/')),
            ],
        ),
        migrations.CreateModel(
            name='Friend',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=120)),
                ('friend', models.CharField(max_length=120)),
                ('nickname', models.CharField(max_length=120)),
            ],
        ),
        migrations.CreateModel(
            name='Msg',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sender', models.CharField(max_length=120)),
                ('receiver', models.CharField(max_length=120)),
                ('message', models.CharField(max_length=1000000)),
                ('date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('file_status', models.BooleanField(default=False)),
                ('file_name', models.CharField(default=None, max_length=1000000, null=True)),
            ],
        ),
    ]
