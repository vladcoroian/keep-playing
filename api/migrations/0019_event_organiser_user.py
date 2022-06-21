# Generated by Django 4.0.5 on 2022-06-20 19:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0018_organiser_blocked_organiser_favourites'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='organiser_user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='organised_events', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]