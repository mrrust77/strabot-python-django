# Generated by Django 5.0 on 2024-01-25 19:40

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("scanner", "0012_symbolrec_is_index"),
    ]

    operations = [
        migrations.AddField(
            model_name="symbolrec",
            name="is_sector",
            field=models.BooleanField(default=False, verbose_name="Is Sector"),
        ),
    ]
