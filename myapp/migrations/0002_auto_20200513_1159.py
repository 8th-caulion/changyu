# Generated by Django 3.0.5 on 2020-05-13 02:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='relation',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='blog',
            name='writer',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
