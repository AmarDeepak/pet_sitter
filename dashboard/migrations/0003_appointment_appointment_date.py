# Generated by Django 4.2.9 on 2024-03-07 02:46

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("dashboard", "0002_appointment_sitter_appointment_user"),
    ]

    operations = [
        migrations.AddField(
            model_name="appointment",
            name="appointment_date",
            field=models.DateField(blank=True, null=True),
        ),
    ]
