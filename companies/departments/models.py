from django.db import models
from django.db.models import UniqueConstraint

from companies.staff.models import Boss, Worker


class Depatament(models.Model):
    """Абстрактная модель департамента"""
    name = models.CharField(max_length=50)
    description = models.CharField()
    boss = models.ForeignKey(
        Boss,
        on_delete=models.SET_NULL,
        null=True,
        related_name="departments",
        verbose_name="Босс",
    )
    workers = models.ManyToManyField(
        Worker,
        related_name="departments",
        through="BossWorkers",
        verbose_name="Сотрудники",
    )

    def __str__(self):
        return self.name


class BigBrother(Depatament):
    """Старшее подразделение"""

    class Meta:
        verbose_name = "Старшее подразделение"

    def __str__(self):
        return self.name


class LittleBrother(models.Model):
    """Младшее подразделение"""

    class Meta:
        verbose_name = "Младшее подразделение"

    def __str__(self):
        return self.name


class Brothers(models.Model):
    """Модель отношения Старший-Младший подразделения"""
    big_bro = models.ForeignKey(
        BigBrother,
        on_delete=models.CASCADE,
        null=True,
        related_name="departments",
        verbose_name="Большой брат"
    )
    little_bro = models.ForeignKey(
        LittleBrother,
        on_delete=models.CASCADE,
        null=True,
        related_name="departments",
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


class CurrentDepartment(models.Model):
    """Отдел/подразделение"""
    little_bro = models.ManyToManyField(
        LittleBrother,
        related_name="departments",
        through="Brothers",
        verbose_name="Младший брат"
    )
    big_bro = models.ForeignKey(
        BigBrother,
        on_delete=models.SET_NULL,
        null=True,
        related_name="departments",
        verbose_name="Большой брат"
    )

    class Meta:
        verbose_name = "Текущее подразделение"
