# Generated by Django 5.0 on 2024-01-04 04:01

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("scanner", "0002_stockindex_symbol"),
    ]

    operations = [
        migrations.AddField(
            model_name="symbolrec",
            name="skip_discord_alerts",
            field=models.BooleanField(
                default=False, verbose_name="Skip Discord Alerts"
            ),
        ),
    ]
