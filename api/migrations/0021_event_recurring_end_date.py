# Generated by Django 4.0.5 on 2022-06-22 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0020_event_creation_ended_event_creation_started'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='recurring_end_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
