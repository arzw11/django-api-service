from dataclasses import dataclass
from datetime import datetime

from src.apps.gear.entities.item_quality import ItemQuality


@dataclass
class Gear:
    id: int # noqa
    title: str
    description: str
    is_prototype: bool

    quality: ItemQuality

    created_at: datetime
    updated_at: datetime | None = None
