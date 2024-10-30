from django.core.exceptions import ValidationError
from django.db import models
from django.utils.translation import gettext_lazy as _


class AppOrder(models.Model):
    title = models.CharField(max_length=200, verbose_name=_("Title"))
    order = models.PositiveIntegerField(default=1, verbose_name=_("Order"))

    def __str__(self):
        return self.title


MODEL_CHOICES = []


def get_models_list():
    from django.apps import apps
    from django.contrib import admin

    models = []
    for i in apps.get_models():
        if i in admin.site._registry:
            models.append(i)
    return models


class ModelOrder(models.Model):
    section = models.ForeignKey(AppOrder, on_delete=models.CASCADE, null=True, related_name="models")
    title = models.CharField(max_length=200, choices=MODEL_CHOICES, verbose_name=_("Title"))
    app_label = models.CharField(max_length=200, default="auth")
    order = models.PositiveIntegerField(default=1, verbose_name=_("Order"))

    class Meta:
        ordering = ("order",)

    def save(self, *args, **kwargs):
        for i in get_models_list():
            if str(i._meta) == self.title:
                self.app_label = i._meta.app_label
        if not self.app_label:
            raise ValidationError("Invalid")
        return super().save(*args, **kwargs)
