from datetime import datetime
from typing import List

from pydantic import BaseModel


class GearSchema(BaseModel):
    title: str
    description: str
    mining_modifier: float
    cooldown_modifier: float
    drop_chance: float
    is_prototype: bool

    created_at: datetime
    updated_at: datetime | None = None


GearListSchema = List[GearSchema]