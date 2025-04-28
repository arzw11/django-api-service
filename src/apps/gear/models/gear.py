from django.db import models

from src.apps.common.models import TimedBaseModel
from src.apps.gear.entities.gear import Gear as GearEntity
from src.apps.gear.entities.item_quality import ItemQuality as ItemQualityEntity
from src.apps.gear.models.item_quality import ItemQuality


class Gear(TimedBaseModel):
    title = models.CharField(
        verbose_name="Название",
        max_length=255,
        blank=False,
        null=False,
    )
    description = models.TextField(
        verbose_name='Описание',
        blank=True,
    )
    is_prototype = models.BooleanField(
        verbose_name="Является образцом",
        default=False,
    )
    quality = models.ForeignKey(
        ItemQuality,
        verbose_name="Качество снаряжения",
        on_delete=models.CASCADE,
        related_name='gears',
    )

    def to_entity(self) -> GearEntity:
        return GearEntity(
            id=self.id,
            title=self.title,
            description=self.description,
            is_prototype=self.is_prototype,
            created_at=self.created_at,
            updated_at=self.updated_at,
            quality=ItemQualityEntity(
                id=self.quality.id,
                title=self.quality.title,
                drop_chance=self.quality.drop_chance,
            ),
        )

    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name = "Cнаряжение"
        verbose_name_plural = "Снаряжения"
