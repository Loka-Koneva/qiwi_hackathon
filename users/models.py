import uuid
from decimal import Decimal

from django.db import models
from django.contrib.auth.models import AbstractUser
from rest_framework_simplejwt.tokens import RefreshToken


STATUS = [
    ("new", "Принята"),
    ("in_work", "В работе"),
    ('done', 'Выполнена')
]


class UIDMixin(models.Model):
    uid = models.UUIDField(primary_key=True, default=uuid.uuid4, blank=True, verbose_name='UID')

    class Meta:
        abstract = True


class Service(UIDMixin):
    name = models.CharField(max_length=150, verbose_name="Название услуги", null=True, blank=True)
    cost = models.DecimalField(verbose_name="Цена услуги", default=Decimal(0.00),
                               max_digits=8, decimal_places=2)
    company = models.ForeignKey("Company", on_delete=models.SET_NULL,
                                verbose_name="Организация", null=True, blank=True)


class Payment(UIDMixin):
    sum = models.DecimalField(verbose_name="Стоимость", decimal_places=2, max_digits=8)
    service_request = models.OneToOneField("ServiceRequest", on_delete=models.SET_NULL,
                                           null=True, verbose_name="Заявка")


class Company(UIDMixin):
    name = models.CharField(max_length=150, verbose_name="Организация", null=True, blank=True)


class User(AbstractUser):
    company = models.ForeignKey("Company", verbose_name="Обслуживающая организация",
                                on_delete=models.SET_NULL, null=True, blank=True)

    @property
    def tokens(self):
        refresh = RefreshToken.for_user(self)
        return {"refresh": str(refresh), "access": str(refresh.access_token)}


class ServiceRequest(UIDMixin):
    user = models.ForeignKey("User", verbose_name="Заказчик",
                             on_delete=models.SET_NULL, null=True)
    service = models.ForeignKey("Service", verbose_name="Услуги",
                                on_delete=models.SET_NULL, null=True)
    status = models.CharField(choices=STATUS, default=STATUS[0], max_length=150)
    grade = models.IntegerField(verbose_name="Оценка")
    comment = models.CharField(max_length=1024, verbose_name="Отзыв", blank=True, null=True)
    file = models.FileField(verbose_name="Файлы", blank=True, null=True)


