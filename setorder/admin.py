from django.contrib import admin

from setorder import models


class ModelOrderInline(admin.TabularInline):
    model = models.ModelOrder
    extra = 0


@admin.register(models.ModelOrder)
class CandidateAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "section", "order")
    list_filter = ("section",)
    list_editable = ("order",)


@admin.register(models.AppOrder)
class CandidateAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "order")
    list_editable = ("order",)
    list_filter = ("title",)
    inlines = [ModelOrderInline]
