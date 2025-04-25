from django.http import HttpRequest
from ninja import Router

from src.api.v1.gear.schemas import GearListSchema

router = Router(tags=["Gear"])


@router.get("", response=GearListSchema)
def get_gear_list_handler(request: HttpRequest) -> GearListSchema:
    return []