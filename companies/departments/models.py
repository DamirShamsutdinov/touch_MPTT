from django.db import models
from django.db.models import UniqueConstraint

# from staff.models import CurrentSpecialist
from staff.models import CurrentSpecialist


class Department(models.Model):
    """Абстрактная модель департамента"""
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=500)

    def __str__(self):
        return self.name


class BigBrother(Department):
    """Старшее подразделение"""

    class Meta:
        verbose_name = "Старшее подразделение"

    def __str__(self):
        return self.name


class LittleBrother(Department):
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
                name="unique_brothers"),
        ]

    def __str__(self):
        return (
            f"Во главе {self.big_bro.name} "
            f"над младшим {self.little_bro.name}"
        )


class CurrentDepartment(models.Model):
    """Отдел/подразделение"""
    BIGBROTHER = "bigbrother"
    LITTLEBROTHER = "littlebrother"
    ROLE = [
        (BIGBROTHER, "Старшее подразделение"),
        (LITTLEBROTHER, "Младшее подразделение")
    ]

    role = models.CharField(
        max_length=16,
        choices=ROLE,
        default=LITTLEBROTHER,
        verbose_name="Роль подразделения",
    )
    if role == 'BIGBROTHER':
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
        ordering = ("id",)
