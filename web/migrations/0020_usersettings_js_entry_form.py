# Generated by Django 3.2.9 on 2021-11-25 18:00

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("web", "0019_week_unique entry"),
    ]

    operations = [
        migrations.AddField(
            model_name="usersettings",
            name="js_entry_form",
            field=models.BooleanField(default=False),
        ),
    ]
