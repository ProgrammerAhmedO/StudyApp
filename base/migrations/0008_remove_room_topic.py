# Generated by Django 3.1.4 on 2022-06-08 12:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0007_auto_20220608_1429'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='room',
            name='Topic',
        ),
    ]
