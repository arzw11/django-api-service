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
    is_prototype = models.BooleanField(
        verbose_name="Является образцом",
        default=False
    )

    def __str__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name = "Cнаряжение"
        verbose_name_plural = "Снаряжения"