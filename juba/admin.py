from django.contrib import admin

from juba import models


class ServiceTypeInline(admin.TabularInline):
    model = models.ServiceType
    extra = 1


class ServiceDetailPhotoInline(admin.TabularInline):
    model = models.ServiceDetailSolo
    extra = 1


from ckeditor.widgets import CKEditorWidget
from django import forms


class PricingAdminForm(forms.ModelForm):
    descriptions = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = models.Pricing
        fields = '__all__'


class ServicePrisingInline(admin.TabularInline):
    forms = PricingAdminForm
    model = models.Pricing
    extra = 1


@admin.register(models.Services)
class ServicesAdmin(admin.ModelAdmin):
    list_display = ("pk", "title")
    inlines = [
        ServiceTypeInline,
        ServiceDetailPhotoInline,
        ServicePrisingInline,
    ]


@admin.register(models.StaticPhoto)
class StaticPageAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Slider)
class SliderAdmin(admin.ModelAdmin):
    list_display = ("pk", "title")

    def has_add_permission(self, request):
        if models.Slider.objects.all().count() >= 1:
            return False
        return True


@admin.register(models.Hashtags)
class HashtagsAdmin(admin.ModelAdmin):
    list_display = ("pk", "title")


@admin.register(models.OurKeys)
class OurKeysAdmin(admin.ModelAdmin):
    list_display = ("pk", "title")


@admin.register(models.StaticSolo)
class StaticSoloAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        if models.StaticSolo.objects.all().count() >= 1:
            return False
        return True


@admin.register(models.ResultNumber)
class ResultNumberAdmin(admin.ModelAdmin):
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
