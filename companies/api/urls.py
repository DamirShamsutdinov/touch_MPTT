from django.urls import include, path, re_path
from rest_framework.routers import SimpleRouter

from api.views import CurrentDepartmentViewSet, CurrentSpecialistViewSet

router = SimpleRouter()
router.register("departments", CurrentDepartmentViewSet, basename="departments")
router.register("employees", CurrentSpecialistViewSet, basename="employees")

urlpatterns = [
    path("", include(router.urls)),
]