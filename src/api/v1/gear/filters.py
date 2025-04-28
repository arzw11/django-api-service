from typing import Optional

from ninja import Schema


class GearFilters(Schema):
    search: Optional[str] = None