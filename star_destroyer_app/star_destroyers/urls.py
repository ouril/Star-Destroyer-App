from rest_framework import routers

from .views import StarDesroyersViewSet

router = routers.SimpleRouter()
router.register(r'ships', StarDesroyersViewSet)

urlpatterns = router.urls