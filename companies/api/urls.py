from django.urls import include, path
from rest_framework.routers import SimpleRouter

from api.views import DepartmentViewSet, PositionViewSet, SpecialistViewSet

router = SimpleRouter()
router.register("department", DepartmentViewSet, basename="department")
router.register("position", PositionViewSet, basename="position")
router.register("specialist", SpecialistViewSet, basename="specialist")

urlpatterns = [
    path("", include(router.urls)),
]
