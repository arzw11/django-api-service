from django.contrib import admin

from src.apps.gear.models.gear import Gear
from src.apps.gear.models.item_quality import ItemQuality


@admin.register(Gear)
class GearAdmin(admin.ModelAdmin):
    list_display = ["id", "title", "is_prototype"]


@admin.register(ItemQuality)
class ItemQualityAdmin(admin.ModelAdmin):
    list_display = ["id", "title", "drop_chance"]
