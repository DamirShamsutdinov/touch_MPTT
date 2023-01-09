import mptt
from django.db import models
from mptt.fields import TreeForeignKey
from mptt.models import MPTTModel

from staff.models import Specialist, Position


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
        blank=False,
        null=True,
        related_name='dep_boss',
        verbose_name='Босс департамента'
    )
    staff = models.ManyToManyField(
        Specialist,
        null=True,
        blank=True,
        default='-пусто-',
        related_name='dep_staff',
        verbose_name='Штатный сотрудник департамента'
    )
    parent = TreeForeignKey(
        'self',
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name='children'
    )

    def __str__(self):
        return self.name

    class MPTTMeta:
        order_insertion_by = ['name']
        db_table = "department"
        verbose_name = "Департамент"
        verbose_name_plural = "Департаменты"

