# Generated by Django 4.2.1 on 2024-01-27 21:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_chat'),
    ]

    operations = [
        migrations.CreateModel(
            name='Doubts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(blank=True, max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('type_of_doubt', models.CharField(max_length=100)),
                ('message', models.TextField()),
            ],
        ),
    ]
