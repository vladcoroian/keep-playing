# Generated by Django 4.0.5 on 2022-06-23 10:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0023_merge_0021_event_recurring_end_date_0022_event_voted'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='recurring_end_date',
        ),
    ]
