# Generated by Django 4.2.8 on 2024-01-12 18:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Professional_Studies', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='professional_studies',
            name='website',
        ),
    ]
