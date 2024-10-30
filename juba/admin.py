from ckeditor.widgets import CKEditorWidget
from django import forms
from django.contrib import admin
from modeltranslation.admin import TranslationAdmin

from juba import models


class ServiceTypeInline(admin.TabularInline):
    model = models.ServiceType
    extra = 1
    fieldsets = (
        ("Russian", {
            "fields": ("title_ru", "description_ru", "title_uz", "description_uz", "photo", "index", "is_top"),
        }),
    )


class ServiceDetailPhotoInline(admin.TabularInline):
    model = models.ServiceDetailSolo
    extra = 1
    fieldsets = (
        ("Russian", {
            "fields": ("description_ru", "description_uz", "photo")
        }),
    )


class PricingAdminForm(forms.ModelForm):
    descriptions = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = models.Pricing
        fields = '__all__'


class ServicePrisingInline(admin.TabularInline):
    # forms = PricingAdminForm
    model = models.Pricing
    extra = 1

    fieldsets = (
        ("Russian", {
            "fields": ("title_ru", "description_ru")
        }),
        ("Uzbek", {
            "fields": ("title_uz", "description_uz")
        }),
    )


class ServiceWorksAdmin(admin.TabularInline):
    model = models.Works
    extra = 1

    fieldsets = (
        ("Russian", {
            "fields": ("short_description_ru", "short_description_uz", "photo")
        }),
    )


@admin.register(models.Services)
class ServicesAdmin(TranslationAdmin, admin.ModelAdmin):
    list_display = ("pk", "title")
    inlines = [
        ServiceTypeInline,
        ServiceDetailPhotoInline,
        ServicePrisingInline,
        ServiceWorksAdmin,
    ]

    fieldsets = (
        ("Russian", {
            "fields": (
                "title_ru", "short_description_ru", "detail_title_ru", "detail_description_ru", "detail_sub_title_ru",
                "detail_sub_description_ru")
        }),
        ("Uzbek", {
            "fields": (
                "title_uz", "short_description_uz", "detail_title_uz", "detail_description_uz", "detail_sub_title_uz",
                "detail_sub_description_uz")
        }),
    )


@admin.register(models.StaticPhoto)
class StaticPageAdmin(TranslationAdmin):
    fieldsets = (
        ("Team/Client", {
            "fields": ("photo", "background_image", "username_uz", "job_title_uz", "photo_type")
        }),
    )


@admin.register(models.Slider)
class SliderAdmin(TranslationAdmin):
    list_display = ("pk", "title")

    def has_add_permission(self, request):
        if models.Slider.objects.all().count() >= 1:
            return False
        return True


@admin.register(models.Hashtags)
class HashtagsAdmin(TranslationAdmin):
    list_display = ("pk", "title")


@admin.register(models.OurKeys)
class OurKeysAdmin(TranslationAdmin):
    list_display = ("pk", "title")


@admin.register(models.StaticSolo)
class StaticSoloAdmin(TranslationAdmin):
    def has_add_permission(self, request):
        if models.StaticSolo.objects.all().count() >= 1:
            return False
        return True


@admin.register(models.ResultNumber)
class ResultNumberAdmin(TranslationAdmin):
    def has_add_permission(self, request):
        if models.ResultNumber.objects.all().count() >= 3:
            return False
        return True


@admin.register(models.Contact)
class OurContactAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        if models.Contact.objects.all().count() >= 1:
            return False
        return True


@admin.register(models.ContactUser)
class ContactUserAdmin(admin.ModelAdmin):
    list_display = ("pk", "name", "phone_number")
