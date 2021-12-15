from rest_framework import routers
from leaderboards.views import RecordViewSet

router = routers.DefaultRouter()
router.register(r'records', RecordViewSet)
