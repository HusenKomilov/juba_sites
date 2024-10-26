from modeltranslation.translator import register, TranslationOptions

from juba import models


@register(models.Services)
class ServicesTranslationOptions(TranslationOptions):
    fields = (
        "title", "short_description", "detail_title", "detail_description", "detail_sub_title",
        "detail_sub_description")


@register(models.ServiceType)
class ServiceTypeTranslationOptions(TranslationOptions):
    fields = ("title", "description")


@register(models.ServiceDetailSolo)
class ServiceDetailSoloTranslationOptions(TranslationOptions):
    fields = ("description",)


@register(models.Works)
class WorksTranslationOptions(TranslationOptions):
    fields = ("short_description",)

# @register(models.)