# Generated by Django 3.0.5 on 2020-05-13 03:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_auto_20200513_1217'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blog',
            old_name='etc',
            new_name='category',
        ),
    ]
