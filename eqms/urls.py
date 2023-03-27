from django.urls import path
from .views import index, welcome, equipment_type, tag_details, oem_details,equipment_data

urlpatterns = [
    path("index/", index, name="home"),
    path("equipment/type/", equipment_type),
    path("equipment/count/", tag_details),
    path("oem/sources/", oem_details),
    path("equipment/data/", equipment_data),
    path("", welcome)
]
