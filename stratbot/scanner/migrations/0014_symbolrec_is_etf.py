# Generated by Django 5.0 on 2024-02-08 05:15

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("scanner", "0013_symbolrec_is_sector"),
    ]

    operations = [
        migrations.AddField(
            model_name="symbolrec",
            name="is_etf",
            field=models.BooleanField(default=False, verbose_name="Is ETF"),
        ),
    ]
