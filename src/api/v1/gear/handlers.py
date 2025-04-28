from django.http import HttpRequest
from ninja import (
    Query,
    Router,
)

from src.api.filters import (
    PaginationIn,
    PaginationOut,
)
from src.api.schemas import (
    ApiResponse,
    ListPaginatedResponse,
)
from src.api.v1.gear.filters import GearFilters
from src.api.v1.gear.schemas import GearSchema
from src.apps.common.filters import PaginationIn as PaginationInEntity
from src.apps.gear.filters.gear import GearFilters as GearFiltersEntity
from src.apps.gear.services.gear import (
    BaseGearService,
    ORMGearService,
)


router = Router(tags=["Gear"])


@router.get("", response=ApiResponse[ListPaginatedResponse[GearSchema]])
def get_gear_list_handler(
    request: HttpRequest,
    filters: Query[GearFilters],
    pagination_in: Query[PaginationIn],
) -> ApiResponse[ListPaginatedResponse[GearSchema]]:
    service: BaseGearService = ORMGearService()
    gear_list = service.get_gear_list(
        filters=GearFiltersEntity(
            search=filters.search,
        ),
        pagination=PaginationInEntity(
            offset=pagination_in.offset,
            limit=pagination_in.limit,
        ),
    )
    gear_count = service.get_gear_count(
        filters=GearFiltersEntity(
            search=filters.search,
        ),
    )

    items = [GearSchema.from_entity(entity=gear) for gear in gear_list]
    pagination = PaginationOut(
        offset=pagination_in.offset,
        limit=pagination_in.limit,
        total=gear_count,
    )

    return ApiResponse(data=ListPaginatedResponse(items=items, pagination=pagination))
