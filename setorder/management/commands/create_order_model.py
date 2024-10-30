from django.core.management.base import BaseCommand

from setorder.models import AppOrder, ModelOrder, get_models_list


class Command(BaseCommand):
    help = "Create model order"

    def handle(self, *args, **options):
        models = get_models_list()
        for m in models:
            if m in (AppOrder, ModelOrder):
                continue
            app = AppOrder.objects.get_or_create(title=m._meta.app_config.verbose_name)[0]
            ModelOrder.objects.get_or_create(
                section=app,
                title=str(m._meta),
            )
