from django.db import models

from src.apps.common.models import TimedBaseModel


class ItemQuality(TimedBaseModel):
    title = models.CharField(
        verbose_name="Название качества",
        max_length=255,
        blank=False,
        null=False,
    )
    drop_chance = models.DecimalField(
        verbose_name="Шанс выпадения",
        max_digits=5,
        decimal_places=2,
        default=0.00,
    )

    def __str__(self) -> str:
        return f"{self.title} - {self.drop_chance}%"

    class Meta:
        verbose_name = "Качество предмета"
        verbose_name_plural = "Качества предметов"
