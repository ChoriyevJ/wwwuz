# Generated by Django 4.2.7 on 2024-03-12 11:42

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("main", "0005_alter_site_test_date"),
    ]

    operations = [
        migrations.AlterField(
            model_name="site",
            name="test_date",
            field=models.DateField(
                default=datetime.datetime(2024, 3, 12, 11, 42, 11, 329670, tzinfo=datetime.timezone.utc)
            ),
        ),
    ]
