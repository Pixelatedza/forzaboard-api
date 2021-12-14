from rest_framework import routers
from leaderboards.views import LeaderboardViewSet, RecordViewSet

router = routers.DefaultRouter()
router.register(r'leaderboards', LeaderboardViewSet)
router.register(r'records', RecordViewSet)
