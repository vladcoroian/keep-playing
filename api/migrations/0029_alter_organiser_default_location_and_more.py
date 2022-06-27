# Generated by Django 4.0.5 on 2022-06-23 15:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0028_remove_coach_qualification_user_qualification'),
    ]

    operations = [
        migrations.AlterField(
            model_name='organiser',
            name='default_location',
            field=models.CharField(blank=True, default='', max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='organiser',
            name='default_role',
            field=models.CharField(blank=True, default='', max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='organiser',
            name='default_sport',
            field=models.CharField(blank=True, default='', max_length=50),
            preserve_default=False,
        ),
    ]