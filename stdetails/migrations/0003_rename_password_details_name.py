# Generated by Django 4.1.5 on 2023-01-22 09:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stdetails', '0002_details'),
    ]

    operations = [
        migrations.RenameField(
            model_name='details',
            old_name='password',
            new_name='name',
        ),
    ]
