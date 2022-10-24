from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models import UniqueConstraint
from django.utils.translation import gettext_lazy as _


class Boss(AbstractUser):
    """Модель Боса"""
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


class Worker(AbstractUser):
    """Модель Сотрудника"""
    salary = models.IntegerField()
    patronymic = models.CharField(_('patronymic'), max_length=150, blank=True)
    boss = models.ManyToManyField(
        Boss,
        through="BossWorkers",
        related_name="worker",
        verbose_name="Босс"
    )
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


class BossWorkers(AbstractUser):
    """Промежуточная модель Босс-Сотрудник"""
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
        verbose_name="Сотрудник",
    )

    class Meta:
        verbose_name = "Сотрудники_босса"
        constraints = [
            UniqueConstraint(
                fields=("boss", "worker"),
                name="unique_boss_workers"),
        ]

    def __str__(self):
        return (
            f"Босс {self.boss.name} над подчиненным {self.worker.name}"
        )
