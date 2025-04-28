from dataclasses import dataclass, field
from datetime import datetime

from src.apps.common.enums import EntityStatus
from src.apps.gear.entities.item_quality import ItemQuality

@dataclass
class Gear:
    id: int
    title: str
    description: str
    is_prototype: bool

    quality: ItemQuality

    created_at: datetime
    updated_at: datetime | None = None


