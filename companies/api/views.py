from rest_framework import viewsets

# from departments.models import CurrentDepartment
# from departments.serializers import CurrentDepartmentSerializer
from departments.models import CurrentDepartment
from departments.serializers import CurrentDepartmentSerializer
from staff.models import CurrentSpecialist
from staff.serializers import CurrentSpecialistSerializer


class CurrentSpecialistViewSet(viewsets.ModelViewSet):
    """Вьюсет для доступа к штату Боссов>"""

    queryset = CurrentSpecialist.objects.all()
    serializer_class = CurrentSpecialistSerializer


class CurrentDepartmentViewSet(viewsets.ModelViewSet):
    """Вьюсет для доступа к Департаментам"""

    queryset = CurrentDepartment.objects.all()
    serializer_class = CurrentDepartmentSerializer
