# Generated by Django 4.0.5 on 2022-06-14 21:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0011_event_role_event_sport'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='role',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='sport',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
