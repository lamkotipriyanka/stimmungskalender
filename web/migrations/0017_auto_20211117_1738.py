# Generated by Django 3.2.9 on 2021-11-17 16:38

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("web", "0016_auto_20211117_1646"),
    ]

    operations = [
        migrations.AddField(
            model_name="week",
            name="week",
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="week",
            name="year",
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
