from datetime import datetime
from typing import List

from pydantic import BaseModel

from src.api.v1.item_quality.schemas import ItemQualitySchema
from src.apps.gear.entities.gear import Gear as GearEntity


class GearSchema(BaseModel):
    id: int # noqa
    title: str
    description: str
    is_prototype: bool
    quality: ItemQualitySchema

    created_at: datetime
    updated_at: datetime | None = None

    @classmethod
    def from_entity(cls, entity: GearEntity) -> "GearSchema":
        return cls(
            id=entity.id,
            title=entity.title,
            description=entity.description,
            is_prototype=entity.is_prototype,
            quality=ItemQualitySchema.from_entity(
                entity=entity.quality,
            ),
            created_at=entity.created_at,
            updated_at=entity.updated_at,
        )


GearListSchema = List[GearSchema]
