from ckeditor.fields import RichTextField
from django.db import models
from django.utils.translation import gettext_lazy as _
from django_resized import ResizedImageField
from juba.choices import PhotoTypeChoices
from phonenumber_field.modelfields import PhoneNumberField
from utils.models import BaseModel


# Service lar uchun
class Services(BaseModel):
    title = models.CharField(max_length=256, verbose_name=_("Title"))
    short_description = models.TextField(verbose_name=_("Short description"))

    def __str__(self):
        return self.title


# service larni detaail uchun content lar
class ServiceType(BaseModel):
    title = models.CharField(max_length=128, verbose_name=_("Title"), )
    description = models.TextField(verbose_name=_("Description"))
    photo = models.ImageField(upload_to="service_type/", verbose_name=_("Photo"))
    services = models.ForeignKey(Services, on_delete=models.CASCADE, related_name="services_types")

    def __str__(self):
        return self.title


# service dagi static rasm va text uchun
class ServiceDetailSolo(BaseModel):
    description = models.TextField(verbose_name=_("Description"))
    photo = models.ImageField(upload_to="service_detail/", verbose_name=_("Photo"))
    service = models.ForeignKey(Services, on_delete=models.CASCADE, related_name="details_solo")


# Servislardagi qilingan ishlari uchun
class Works(BaseModel):
    short_description = models.TextField()
    photo = models.ImageField(upload_to="works/", verbose_name=_("Photo"))
    services = models.ForeignKey(Services, on_delete=models.CASCADE, related_name="works")


# Tariflar uchun
class Pricing(BaseModel):
    title = models.CharField(max_length=128)
    description = RichTextField()
    price = models.IntegerField(default=0)
    service = models.ForeignKey(Services, on_delete=models.CASCADE, related_name="prices")

    def __str__(self):
        return self.title


# Hashtaglar uchun
class Hashtags(BaseModel):
    title = models.CharField(max_length=128, verbose_name=_("Hashtag"))

    def __str__(self):
        return self.title


# Bitirib bergan ishlari uchun
class OurKeys(BaseModel):
    title = models.CharField(max_length=128, verbose_name=_("Title"))
    photo = models.ImageField(upload_to="clients/", verbose_name=_("Main Photo"))
    url = models.URLField(verbose_name=_("Project URL"), null=True, blank=True)
    hashtags = models.ManyToManyField(Hashtags, blank=True, related_name="hastags", verbose_name=_("Hashtags"))
    service = models.ForeignKey(Services, on_delete=models.CASCADE, related_name="services", verbose_name=_("Services"))

    def __str__(self):
        return self.title


# SEO uchun
class SEOText(BaseModel):
    title = models.CharField(_("Title"), max_length=255)
    description = models.TextField(_("Description"))
    keywords = models.CharField(_("Keywords"), max_length=255)
    image = ResizedImageField(
        verbose_name=_("Cover Image"),
        upload_to="cover_images/",
        blank=True,
        null=True,
    )
    slug = models.SlugField(max_length=256, unique=True, db_index=True)

    class Meta:
        verbose_name = _("SEO Text")
        verbose_name_plural = _("SEO Texts")
        ordering = ("-created_at",)


# klientlar kontaktlarnini kiritishi uchun
class ContactUser(BaseModel):
    name = models.CharField(max_length=128, verbose_name=_("Name"))
    phone_number = PhoneNumberField(unique=True)

    def __str__(self):
        return self.name

    """Userlar contact kiritishi uchun forma"""


# klientlar va jamoa rasmlari uchun
class StaticPhoto(BaseModel):
    photo = models.ImageField(upload_to="team/", verbose_name=_("Photo"))
    photo_type = models.CharField(max_length=128, verbose_name=_("Photo Type"), choices=PhotoTypeChoices.choices)

    def __str__(self):
        return self.photo_type

    """Bosh sahifa uchun static rasm uchun"""


# bosh sahifa uchun natijalar uchun
class ResultNumber(BaseModel):
    title = models.CharField(max_length=128, verbose_name=_("Title"))
    result = models.IntegerField(verbose_name=_("Result"))

    def __str__(self):
        return self.title


# bosh sahifadagi carusel uchun
class Slider(BaseModel):
    title = models.CharField(max_length=256, verbose_name=_("Title"))
    short_description = models.TextField()
    photo = models.ImageField(
        verbose_name=_("Photo"),
        upload_to="slider/",
        blank=True,
        null=True,
    )

    def __str__(self):
        return self.title


# JUBA ni kontaktlari uchun
class Contact(BaseModel):
    phone_number = PhoneNumberField(unique=True, verbose_name=_("Phone Number"))
    longitude = models.DecimalField(default=0, max_digits=9, decimal_places=6)
    latitude = models.DecimalField(default=0, max_digits=9, decimal_places=6)
    email = models.CharField(max_length=128, verbose_name=_("Email"))
    telegram_url = models.CharField(max_length=128, verbose_name=_("Telegram Username"))
    instagram_url = models.CharField(max_length=128, verbose_name=_("Instagram Link"))
    facebook_url = models.CharField(max_length=128, verbose_name=_("Facebook Link"))

    def __str__(self):
        return self.email


# bosh sahifadagi statik rasm va text uchun
class StaticSolo(BaseModel):
    photo = models.ImageField(upload_to="solo./")
    description = models.TextField()
