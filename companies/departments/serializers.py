from rest_framework import serializers

from departments.models import Department


class DepartmentSerializer(serializers.ModelSerializer):
    """Сериализатор модели отношения Младшее Подразделение"""

    class Meta:
        fields = "__all__"
        model = Department
