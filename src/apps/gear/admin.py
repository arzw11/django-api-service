from django.contrib import admin
from src.apps.gear.models.gear import Gear


@admin.register(Gear)
class GearAdmin(admin.ModelAdmin):
    list_display = ["id", "title", "mining_modifier", "cooldown_modifier",]