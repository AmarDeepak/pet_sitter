# Generated by Django 4.2.9 on 2024-02-25 09:53

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="petowner",
            name="zipcode",
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
    ]