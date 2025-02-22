# Generated by Django 5.1.2 on 2024-10-20 07:37

import ckeditor.fields
import django.db.models.deletion
import django_resized.forms
import phonenumber_field.modelfields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Contact",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "phone_number",
                    phonenumber_field.modelfields.PhoneNumberField(
                        max_length=128,
                        region=None,
                        unique=True,
                        verbose_name="Phone Number",
                    ),
                ),
                (
                    "longitude",
                    models.DecimalField(decimal_places=6, default=0, max_digits=9),
                ),
                (
                    "latitude",
                    models.DecimalField(decimal_places=6, default=0, max_digits=9),
                ),
                ("email", models.CharField(max_length=128, verbose_name="Email")),
                (
                    "telegram_url",
                    models.CharField(max_length=128, verbose_name="Telegram Username"),
                ),
                (
                    "instagram_url",
                    models.CharField(max_length=128, verbose_name="Instagram Link"),
                ),
                (
                    "facebook_url",
                    models.CharField(max_length=128, verbose_name="Facebook Link"),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="ContactUser",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("name", models.CharField(max_length=128, verbose_name="Name")),
                (
                    "phone_number",
                    phonenumber_field.modelfields.PhoneNumberField(
                        max_length=128, region=None, unique=True
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="Hashtags",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("title", models.CharField(max_length=128, verbose_name="Hashtag")),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="ResultNumber",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("title", models.CharField(max_length=128, verbose_name="Title")),
                ("result", models.IntegerField(verbose_name="Result")),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="SEOText",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("title", models.CharField(max_length=255, verbose_name="Title")),
                ("description", models.TextField(verbose_name="Description")),
                ("keywords", models.CharField(max_length=255, verbose_name="Keywords")),
                (
                    "image",
                    django_resized.forms.ResizedImageField(
                        blank=True,
                        crop=None,
                        force_format=None,
                        keep_meta=True,
                        null=True,
                        quality=-1,
                        scale=None,
                        size=[1920, 1080],
                        upload_to="cover_images/",
                        verbose_name="Cover Image",
                    ),
                ),
                ("slug", models.SlugField(max_length=256, unique=True)),
            ],
            options={
                "verbose_name": "SEO Text",
                "verbose_name_plural": "SEO Texts",
                "ordering": ("-created_at",),
            },
        ),
        migrations.CreateModel(
            name="Services",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("title", models.CharField(max_length=256, verbose_name="Title")),
                (
                    "short_description",
                    models.TextField(verbose_name="Short description"),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="Slider",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("title", models.CharField(max_length=256, verbose_name="Title")),
                ("short_description", models.TextField()),
                (
                    "photo",
                    models.ImageField(
                        blank=True, null=True, upload_to="slider/", verbose_name="Photo"
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="StaticPhoto",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("photo", models.ImageField(upload_to="team/", verbose_name="Photo")),
                (
                    "photo_type",
                    models.CharField(
                        choices=[("team", "Team"), ("clients", "Clients")],
                        max_length=128,
                        verbose_name="Photo Type",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="StaticSolo",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("photo", models.ImageField(upload_to="solo./")),
                ("description", models.TextField()),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="ServiceDetailSolo",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("description", models.TextField(verbose_name="Description")),
                (
                    "photo",
                    models.ImageField(
                        upload_to="service_detail/", verbose_name="Photo"
                    ),
                ),
                (
                    "service",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="details_solo",
                        to="juba.services",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="Pricing",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("title", models.CharField(max_length=128)),
                ("description", ckeditor.fields.RichTextField()),
                ("price", models.IntegerField(default=0)),
                (
                    "service",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="prices",
                        to="juba.services",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="OurKeys",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("title", models.CharField(max_length=128, verbose_name="Title")),
                (
                    "photo",
                    models.ImageField(upload_to="clients/", verbose_name="Main Photo"),
                ),
                (
                    "url",
                    models.URLField(blank=True, null=True, verbose_name="Project URL"),
                ),
                (
                    "hashtags",
                    models.ManyToManyField(
                        blank=True,
                        related_name="hastags",
                        to="juba.hashtags",
                        verbose_name="Hashtags",
                    ),
                ),
                (
                    "service",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="services",
                        to="juba.services",
                        verbose_name="Services",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="ServiceType",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("title", models.CharField(max_length=128, verbose_name="Title")),
                ("description", models.TextField(verbose_name="Description")),
                (
                    "photo",
                    models.ImageField(upload_to="service_type/", verbose_name="Photo"),
                ),
                (
                    "services",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="services_types",
                        to="juba.services",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="Works",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("short_description", models.TextField()),
                ("photo", models.ImageField(upload_to="works/", verbose_name="Photo")),
                (
                    "services",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="works",
                        to="juba.services",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
    ]
