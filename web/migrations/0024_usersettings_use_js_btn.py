# Generated by Django 4.1.4 on 2023-01-01 20:01

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("web", "0023_usermoodcolorsettings_remove_week_unique entry_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="usersettings",
            name="use_js_btn",
            field=models.BooleanField(default=True),
        ),
    ]
