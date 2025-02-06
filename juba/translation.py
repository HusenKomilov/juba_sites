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


@register(models.Pricing)
class PricingTranslationOptions(TranslationOptions):
    fields = ("title", "description")


@register(models.Hashtags)
class HashtagsTranslationOptions(TranslationOptions):
    fields = ("title",)


@register(models.OurKeys)
class OurKeysTranslationOptions(TranslationOptions):
    fields = ("title",)


@register(models.StaticPhoto)
class StaticPhotoTranslationOptions(TranslationOptions):
    fields = ("username", "job_title")


@register(models.ResultNumber)
class ResultNumberTranslationOptions(TranslationOptions):
    fields = ("title",)


@register(models.Slider)
class SliderTranslationOptions(TranslationOptions):
    fields = ("title", "short_description",)


@register(models.StaticSolo)
class StaticSoloTranslationOptions(TranslationOptions):
    fields = ("description",)

@register(models.SEOText)
class SEOTextTranslationOptions(TranslationOptions):
    fields = ("title", "description", "keywords")

