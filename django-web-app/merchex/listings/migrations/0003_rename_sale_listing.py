# Generated by Django 4.1 on 2024-10-12 14:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0002_sale'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Sale',
            new_name='Listing',
        ),
    ]