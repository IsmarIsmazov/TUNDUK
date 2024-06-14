from rest_framework.routers import DefaultRouter
from .views import SecurityServersViewSet, ServiceViewSet, SubSystemsViewSet

router = DefaultRouter()
router.register('security_servers', SecurityServersViewSet)
router.register('service', ServiceViewSet)
router.register('sub_system', SubSystemsViewSet)


urlpatterns = router.urls