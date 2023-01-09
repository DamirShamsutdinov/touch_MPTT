from django.db import models
from django.db.models import UniqueConstraint


class Position(models.Model):
    """Модель штатной позиции сотрудника"""
    name = models.CharField(max_length=100, verbose_name='Название штатки')
    salary = models.PositiveSmallIntegerField(verbose_name='Заработная плата')
    description = models.TextField(verbose_name='Обязанности и т.п.')

    class Meta:
        db_table = "position"
        ordering = ("name",)
        verbose_name = "Штатная позиция"
        verbose_name_plural = "Штатные позиции"

    def __str__(self):
        return self.name


class Specialist(models.Model):
    """Модель сотрудника компании"""
    MALE = 'M'
    FEMALE = 'F'
    GENDERS = [
        (MALE, 'Мужчина'),
        (FEMALE, 'Женщина'),
    ]
    email = models.EmailField(unique=True)
    full_name = models.CharField(max_length=255, verbose_name='ФИО')
    gender = models.CharField(
        max_length=1,
        choices=GENDERS,
        verbose_name='Половой признак'
    )
    position = models.ForeignKey(
        Position,
        on_delete=models.CASCADE,
        related_name='spec_position',
        verbose_name='Позиция в штатке'
    )

    class Meta:
        db_table = "specialist"
        ordering = ("id",)
        verbose_name = "Специалист"
        verbose_name_plural = "Специалисты"

        constraints = [
            UniqueConstraint(
                fields=("full_name", "position"),
                name="unique_specpositionlist")
        ]

    def __str__(self):
        return f"{self.full_name} на позиции - {self.position}"