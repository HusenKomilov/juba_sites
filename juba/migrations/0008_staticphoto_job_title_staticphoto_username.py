# Generated by Django 5.1.2 on 2024-10-26 06:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("juba", "0007_alter_works_short_description"),
    ]

    operations = [
        migrations.AddField(
            model_name="staticphoto",
            name="job_title",
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AddField(
            model_name="staticphoto",
            name="username",
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
    ]
