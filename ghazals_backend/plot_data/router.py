from rest_framework import routers
from .viewsets import GhazalsViewSet, CommandoViewSet

app_name =  "plot_data"

router = routers.DefaultRouter()
router.register(r'ghazal',GhazalsViewSet,basename='ghazal')
router.register(r'commando',CommandoViewSet,basename='commando')