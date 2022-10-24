from rest_framework import serializers

from companies.staff.models import Boss, Worker, BossWorkers, CurrentSpecialist


class BossSerializer(serializers.ModelSerializer):
    """Сериализатор модели Босс"""

    class Meta:
        fields = "__all__"
        model = Boss


class WorkerSerializer(serializers.ModelSerializer):
    """Сериализатор модели Сотрудник"""

    class Meta:
        fields = "__all__"
        model = Worker


class BossWorkersSerializer(serializers.ModelSerializer):
    """Сериализатор модели отношения Босс-Сотрудник"""

    class Meta:
        fields = "__all__"
        model = BossWorkers


class CurrentSpecialistSerializer(serializers.ModelSerializer):
    """Сериализатор текущего спецаилиста"""

    class Meta:
        fields = "__all__"
        model = CurrentSpecialist

