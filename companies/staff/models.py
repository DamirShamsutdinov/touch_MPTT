from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models import UniqueConstraint
from django.utils.translation import gettext_lazy as _


class Specialist(AbstractUser):
    """Абстрактная модель сотрудника компании"""
    salary = models.IntegerField()
    patronymic = models.CharField(_('patronymic'), max_length=150, blank=True)
    REQUIRED_FIELDS = [
        'last_name',
        'first_name',
        'patronymic',
        'email',
        'salary'
    ]

    class Meta:
        ordering = ("id",)

    def __str__(self):
        return self.first_name + self.last_name


class Boss(Specialist):
    """Модель Боса"""

    class Meta:
        verbose_name = "Босс"

    def __str__(self):
        return self.first_name + self.last_name


class Worker(AbstractUser):
    """Модель Штатного сотрудника"""

    class Meta:
        verbose_name = "Штатный сотрудник"

    def __str__(self):
        return self.first_name + self.last_name


class BossWorkers(models.Model):
    """Промежуточная модель Босс-Штатный"""
    boss = models.ForeignKey(
        Boss,
        on_delete=models.CASCADE,
        null=True,
        related_name="bossworkers",
        verbose_name="Босс",
    )
    worker = models.ForeignKey(
        Worker,
        on_delete=models.CASCADE,
        null=True,
        related_name="bossworkers",
        verbose_name="Штатный сотрудник",
    )

    class Meta:
        verbose_name = "Босс_Штатные_спецы"
        constraints = [
            UniqueConstraint(
                fields=("boss", "worker"),
                name="unique_boss_workers"),
        ]

    def __str__(self):
        return (
            f"Босс {self.boss.name} над подчиненным {self.worker.name}"
        )

class CurrentSpecialist(models.Model):
    """Текущий специалист"""
    worker = models.ManyToManyField(
        Worker,
        related_name="departments",
        through="BossWorkers",
        verbose_name="Штатный сотрудник"
    )
    boss = models.ForeignKey(
        Boss,
        on_delete=models.SET_NULL,
        null=True,
        related_name="departments",
        verbose_name="Босс"
    )

    class Meta:
        verbose_name = "Текущее подразделение"