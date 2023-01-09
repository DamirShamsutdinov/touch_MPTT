from rest_framework import serializers

from staff.models import Specialist


class SpecialistSerializer(serializers.ModelSerializer):
    """Сериализатор спецаилиста"""

    class Meta:
        fields = "__all__"
        model = Specialist
