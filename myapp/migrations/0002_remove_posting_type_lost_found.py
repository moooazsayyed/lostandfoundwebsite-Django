# Generated by Django 4.2.4 on 2023-09-30 18:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='posting',
            name='type_lost_found',
        ),
    ]
