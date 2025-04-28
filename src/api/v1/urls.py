from ninja import Router

from src.api.v1.gear.handlers import router as gear_router


router = Router(tags=["v1"])

router.add_router("gear/", gear_router)
