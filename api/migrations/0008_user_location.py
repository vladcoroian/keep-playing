# Generated by Django 4.0.5 on 2022-06-14 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='location',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
    ]
