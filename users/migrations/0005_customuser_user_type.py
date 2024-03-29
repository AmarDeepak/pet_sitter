# Generated by Django 4.2.9 on 2024-03-10 08:32

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0004_alter_petowner_user_type_alter_petsitter_user_type"),
    ]

    operations = [
        migrations.AddField(
            model_name="customuser",
            name="user_type",
            field=models.TextField(
                blank=True,
                choices=[("petowner", "petowner"), ("petsitter", "petsitter")],
                default="petowner",
                null=True,
            ),
        ),
    ]
