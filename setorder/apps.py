from django.apps import AppConfig


class SetorderConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "setorder"

    def ready(self):
        from .models import get_models_list, MODEL_CHOICES
        for model in get_models_list():
            MODEL_CHOICES.append((str(model._meta), model._meta.verbose_name_plural))
