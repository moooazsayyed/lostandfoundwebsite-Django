# Generated by Django 4.2.4 on 2023-10-10 07:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0007_alter_listing_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='lost_and_found',
            field=models.CharField(choices=[('lost', 'Lost'), ('found', 'Found')], max_length=10),
        ),
    ]
