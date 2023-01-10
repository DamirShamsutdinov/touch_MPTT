from django.db import models
from django.db.models import UniqueConstraint, ForeignKey
from mptt.fields import TreeForeignKey
from mptt.models import MPTTModel


class Position(models.Model):
    """Модель штатной позиции сотрудника"""
    name = models.CharField(max_length=100, verbose_name='Название штатки')
    salary = models.PositiveSmallIntegerField(verbose_name='Заработная плата')
    description = models.TextField(verbose_name='Обязанности и т.п.')
    department = TreeForeignKey(
        'Department',
        on_delete=models.PROTECT,
        related_name='dep_position',
        verbose_name='Департамент'

    )

    class Meta:
        db_table = "position"
        ordering = ("name",)
        verbose_name = "Позиция в штатке"

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
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name='position_spec',
        verbose_name='Позиция в штатке'
    )

    class Meta:
        db_table = "specialist"
        ordering = ("id",)
        verbose_name = "Специалист"
        verbose_name_plural = "Специалисты"

    def __str__(self):
        return f'{self.full_name} - {self.position}'


class Department(MPTTModel):
    """Модель департамента"""
    name = models.CharField(
        max_length=100,
        unique=True,
        verbose_name='Название департамента'
    )
    description = models.TextField(verbose_name='Описание департамента')
    boss = models.ForeignKey(
        Specialist,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='dep_boss',
        verbose_name='Босс департамента'
    )
    staff = models.ManyToManyField(
        Specialist,
        blank=True,
        related_name='dep_staff',
        verbose_name='Штатный сотрудник департамента'
    )
    parent = TreeForeignKey(
        'self',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='children'
    )

    class MPTTMeta:
        order_insertion_by = ['name']
        db_table = "department"
        verbose_name = "Штатная позиция"
        verbose_name_plural = "Штатные позиции"

    def __str__(self):
        return self.name
