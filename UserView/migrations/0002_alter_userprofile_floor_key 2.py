# Generated by Django 4.0.2 on 2022-02-27 02:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('UserView', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='floor_key',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='UserView.floor'),
        ),
    ]
