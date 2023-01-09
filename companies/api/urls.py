from django.urls import include, path, re_path
from rest_framework.routers import SimpleRouter

from api.views import PositionViewSet, DepartmentViewSet, SpecialistViewSet

router = SimpleRouter()
router.register("department", DepartmentViewSet, basename="department")
router.register("position", PositionViewSet, basename="position")
router.register("specialist", SpecialistViewSet, basename="specialist")

urlpatterns = [
    path("", include(router.urls)),
]