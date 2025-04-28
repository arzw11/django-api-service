from dataclasses import dataclass


@dataclass(frozen=True)
class GearFilters:
    search: str | None = None
