from rest_framework import serializers

from departments.models import BigBrother, LittleBrother, Brothers, \
    CurrentDepartment


class BigBrotherSerializer(serializers.ModelSerializer):
    """Сериализатор модели отношения Старшее Подразделение"""

    class Meta:
        fields = "__all__"
        model = BigBrother


class LittleBrotherSerializer(serializers.ModelSerializer):
    """Сериализатор модели отношения Младшее Подразделение"""

    class Meta:
        fields = "__all__"
        model = LittleBrother


class BrothersSerializer(serializers.ModelSerializer):
    """Сериализатор модели отношения Старшее-Младшее Подразделения"""

    class Meta:
        fields = "__all__"
        model = Brothers


class CurrentDepartmentSerializer(serializers.ModelSerializer):
    """Сериализатор модели текущего Подразделения"""

    class Meta:
        fields = "__all__"
        model = CurrentDepartment
