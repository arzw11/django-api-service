from abc import ABC, abstractmethod
from typing import Iterable

from django.db.models import Q

from src.apps.common.filters import PaginationIn
from src.apps.gear.entities.gear import Gear
from src.apps.gear.models.gear import Gear as GearDTO
from src.apps.gear.filters.gear import GearFilters


class BaseGearService(ABC):
    @abstractmethod
    def get_gear_list(
        self,
        filters: GearFilters,
        pagination: PaginationIn
    ) -> Iterable[Gear]:
        ...

    @abstractmethod
    def get_gear_count(self, filters: GearFilters) -> int:
        ...

class ORMGearService(BaseGearService):
    def _build_gear_query(self, filters: GearFilters) -> Q:
        query = Q(is_prototype=True)

        if filters.search is not None:
            query &= (
                Q(title__icontains=filters.search) |
                Q(description__icontains=filters.search)
            )

        return query
    
    def get_gear_list(
        self,
        filters: GearFilters,
        pagination: PaginationIn
    ) -> Iterable[Gear]:
        query = self._build_gear_query(filters=filters)
        qs = GearDTO.objects.filter(query)[
            pagination.offset:pagination.offset + pagination.limit
        ]

        return [gear.to_entity() for gear in qs]
    
    def get_gear_count(self, filters: GearFilters):
        query = self._build_gear_query(filters=filters)
        
        return GearDTO.objects.filter(query).count()