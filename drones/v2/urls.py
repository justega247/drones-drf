from django.urls import path
from drones.v2 import views as views_v2
from ..views import (
    DroneList,
    DroneCategoryList,
    DroneCategoryDetail,
    DroneDetail,
    PilotList,
    PilotDetail,
    CompetitionList,
    CompetitionDetail,
)

app_name = 'drones'
urlpatterns = [
    path('vehicle-categories/', DroneCategoryList.as_view(), name=DroneCategoryList.name),
    path('vehicle-categories/<int:pk>', DroneCategoryDetail.as_view(), name=DroneCategoryDetail.name),
    path('vehicles/', DroneList.as_view(), name=DroneList.name),
    path('vehicles/<int:pk>', DroneDetail.as_view(), name=DroneDetail.name),
    path('pilots/', PilotList.as_view(), name=PilotList.name),
    path('pilots/<int:pk>', PilotDetail.as_view(), name=PilotDetail.name),
    path('competitions/', CompetitionList.as_view(), name=CompetitionList.name),
    path('competitions/<int:pk>', CompetitionDetail.as_view(), name=CompetitionDetail.name),
    path('', views_v2.ApiRootVersion2.as_view(), name=views_v2.ApiRootVersion2.name)
]
