from django.db import models

from src.apps.common.models import TimedBaseModel


class Gear(TimedBaseModel):
    title = models.CharField(
        verbose_name="Название",
        max_length=255,
        blank=False,
        null=False
    )
    description = models.TextField(
        verbose_name='Описание',
        blank=True,
    )
    mining_modifier = models.FloatField(
        verbose_name="Модификатор добычи",
        blank=False,
        default=1,
    )
    cooldown_modifier = models.FloatField(
        verbose_name="Модификатор перезарядки",
        blank=False,
        default=1,
    )
    drop_chance = models.FloatField(
        verbose_name="Шанс выпадения",
        blank=False,
        null=False
    )
    is_prototype = models.BooleanField(
        verbose_name="Является образцом",
        default=False
    )

    def __str__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name = "Cнаряжение"
        verbose_name_plural = "Снаряжения"