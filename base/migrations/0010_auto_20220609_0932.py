# Generated by Django 3.1.4 on 2022-06-09 07:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0009_room_topic'),
    ]

    operations = [
        migrations.RenameField(
            model_name='room',
            old_name='Topic',
            new_name='topic',
        ),
        migrations.AlterField(
            model_name='topic',
            name='name',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
    ]
