# Generated by Django 4.0.2 on 2022-02-27 04:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('UserView', '0010_userprofile_floor_key'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='floor',
        ),
    ]
