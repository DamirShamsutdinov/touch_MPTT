from django.db import models
from django.db.models import UniqueConstraint

from staff.models import CurrentSpecialist


class Depatament(models.Model):
    """Абстрактная модель департамента"""
    name = models.CharField(max_length=50)
    description = models.CharField()
    specialist = models.ManyToManyField(
        CurrentSpecialist,
        related_name="department",
        through="DepSpec",
        verbose_name="Сотрудники",
    )

    def __str__(self):
        return self.name


class DepSpec(models.Model):
    specialist = models.ForeignKey(
        CurrentSpecialist,
        on_delete=models.CASCADE,
        null=True,
        related_name="depspec",
        verbose_name="Специалист"
    )
    department = models.ForeignKey(
        Depatament,
        on_delete=models.CASCADE,
        null=True,
        related_name="depspec",
        verbose_name="Подразделение"
    )

    class Meta:
        verbose_name = "Специалист_Департамент_отношения"
        constraints = [
            UniqueConstraint(
                fields=("specialist", "department"),
                name="unique_depspec"),
        ]

    def __str__(self):
        return (
            f"Специалист {self.specialist.name} "
            f"относится к подразделению {self.department.name}"
        )


class BigBrother(Depatament):
    """Старшее подразделение"""

    class Meta:
        verbose_name = "Старшее подразделение"

    def __str__(self):
        return self.name


class LittleBrother(Depatament):
    """Младшее подразделение"""

    class Meta:
        verbose_name = "Младшее подразделение"

    def __str__(self):
        return self.name


class CurrentDepartment(models.Model):
    """Отдел/подразделение"""
    little_bro = models.ManyToManyField(
        LittleBrother,
        related_name="currdep",
        through="Brothers",
        verbose_name="Младший брат"
    )
    big_bro = models.ForeignKey(
        BigBrother,
        on_delete=models.SET_NULL,
        null=True,
        related_name="currdep",
        verbose_name="Большой брат"
    )

    class Meta:
        verbose_name = "Текущее подразделение"


class Brothers(models.Model):
    """Модель отношения Старший-Младший подразделения"""
    big_bro = models.ForeignKey(
        BigBrother,
        on_delete=models.CASCADE,
        null=True,
        related_name="brothers",
        verbose_name="Большой брат"
    )
    little_bro = models.ForeignKey(
        LittleBrother,
        on_delete=models.CASCADE,
        null=True,
        related_name="brothers",
        verbose_name="Младший брат"
    )

    class Meta:
        verbose_name = "Старший_Младший_подразделения"
        constraints = [
            UniqueConstraint(
                fields=("big_bro", "little_bro"),
                name="unique_departments"),
        ]

    def __str__(self):
        return (
            f"Во главе {self.big_bro.name} "
            f"над младшим {self.little_bro.name}"
        )
