from django.http import HttpRequest
from django.urls import path
from ninja import NinjaAPI

from src.api.schemas import PingResponseSchema
from src.api.v1.urls import router as v1_router


api = NinjaAPI()

api.add_router("v1/", v1_router)


@api.get("/ping", response=PingResponseSchema)
def ping(request: HttpRequest):
    return PingResponseSchema(result=True)


urlpatterns = [
    path("", api.urls),
]
