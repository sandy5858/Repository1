# Generated by Django 3.0.2 on 2020-02-06 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0010_auto_20200206_2059'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orders',
            name='prc',
        ),
        migrations.AddField(
            model_name='orders',
            name='amount',
            field=models.CharField(default='', max_length=10),
        ),
    ]
