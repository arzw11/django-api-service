from pydantic import BaseModel

from src.apps.gear.entities.item_quality import ItemQuality as ItemQualityEntity


class ItemQualitySchema(BaseModel):
    id: int # noqa
    title: str
    drop_chance: float

    @classmethod
    def from_entity(cls, entity: ItemQualityEntity) -> "ItemQualitySchema":
        return cls(
            id=entity.id,
            title=entity.title,
            drop_chance=entity.drop_chance,
        )
