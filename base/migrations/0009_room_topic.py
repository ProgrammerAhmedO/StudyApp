# Generated by Django 3.1.4 on 2022-06-09 07:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0008_remove_room_topic'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='Topic',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='base.topic'),
        ),
    ]
