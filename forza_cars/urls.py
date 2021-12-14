from rest_framework import routers
from forza_cars.views import BrandViewSet, CarViewSet

router = routers.DefaultRouter()
router.register(r'brands', BrandViewSet)
router.register(r'cars', CarViewSet)
