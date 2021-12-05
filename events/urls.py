from rest_framework import routers
from events.views import EventViewSet, EventKindViewSet, LocationViewSet

router = routers.DefaultRouter()
router.register(r'events', EventViewSet)
router.register(r'event-kinds', EventKindViewSet)
router.register(r'locations', LocationViewSet)
