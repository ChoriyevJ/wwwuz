# Generated by Django 4.2.7 on 2024-03-12 05:44

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("main", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="site",
            name="in_tasix",
            field=models.BooleanField(default=False),
        ),
    ]
