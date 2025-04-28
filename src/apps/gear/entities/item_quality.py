from dataclasses import dataclass

@dataclass(frozen=True)
class ItemQuality:
    id: int
    title: str
    drop_chance: float
