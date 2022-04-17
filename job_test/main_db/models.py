from django.db import models


class Customer(models.Model):
    name = models.CharField('name_customer', max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Автодиллеры'
        verbose_name_plural = 'Автодиллеры'

