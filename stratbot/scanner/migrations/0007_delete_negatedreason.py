# Generated by Django 5.0 on 2024-01-08 02:22

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("scanner", "0006_remove_setup_negated_reasons"),
    ]

    operations = [
        migrations.DeleteModel(
            name="NegatedReason",
        ),
    ]
