# Generated by Django 5.0 on 2024-01-14 19:04

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("scanner", "0009_providermeta"),
    ]

    operations = [
        migrations.RenameField(
            model_name="providermeta",
            old_name="provider_name",
            new_name="name",
        ),
        migrations.RenameField(
            model_name="providermeta",
            old_name="main_model",
            new_name="symbolrec",
        ),
    ]
