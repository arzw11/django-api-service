from dataclasses import dataclass


@dataclass(frozen=True)
class ItemQuality:
    id: int # noqa
    title: str
    drop_chance: float
