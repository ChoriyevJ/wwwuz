# Generated by Django 4.2.7 on 2024-03-12 10:38

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("main", "0002_site_in_tasix"),
    ]

    operations = [
        migrations.AddField(
            model_name="category",
            name="code",
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="statistic",
            name="statistic_type",
            field=models.CharField(
                choices=[
                    ("Visitors", "Visitors"),
                    ("Browsers", "Browser"),
                    ("Providers", "Provider"),
                    ("Countries", "Country"),
                    ("Oses", "Os"),
                    ("ScreensResolution", "Screen Res"),
                    ("EntryPoints", "Entry Point"),
                    ("ExitsPoints", "Exit Point"),
                    ("SearchEngines", "Search Engine"),
                    ("Devices", "Device"),
                ],
                max_length=31,
            ),
        ),
    ]
