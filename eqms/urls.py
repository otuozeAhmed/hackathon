from django.urls import path
from .views import index, welcome, equipment_type, tag_details, oem_details

urlpatterns = [
    path("index/", index, name="home"),
    path("equipment/type/", equipment_type),
    path("tag/data/", tag_details),
    path("oem/data/", oem_details),
    path("", welcome)
]
