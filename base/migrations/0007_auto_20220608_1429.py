# Generated by Django 3.1.4 on 2022-06-08 12:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0006_auto_20220608_1426'),
    ]

    operations = [
        migrations.RenameField(
            model_name='room',
            old_name='topic',
            new_name='Topic',
        ),
    ]
