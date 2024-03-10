# Generated by Django 4.2.9 on 2024-03-04 08:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0003_petowner_user_type_petsitter_user_type"),
        ("dashboard", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="appointment",
            name="sitter",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.PROTECT,
                to="users.petsitter",
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="appointment",
            name="user",
            field=models.ForeignKey(
                default=2,
                on_delete=django.db.models.deletion.PROTECT,
                to="users.petowner",
            ),
            preserve_default=False,
        ),
    ]