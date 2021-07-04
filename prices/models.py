from django.db import models


class CardPrice(models.Model):
    cp_price = models.CharField(max_length=50, verbose_name='Card Price')
    cp_description = models.CharField(max_length=50, verbose_name='Card Description')

    def __str__(self):
        return self.cp_price

    class Meta:
        verbose_name = 'Card Price'
        verbose_name_plural = 'Card Prices'


class TablePrice(models.Model):
    tp_name = models.CharField(max_length=50, verbose_name='Service Description')
    tp_old_price = models.CharField(max_length=50, verbose_name='Service Old Price')
    tp_new_price = models.CharField(max_length=50, verbose_name='Service New Price')

    def __str__(self):
        return self.tp_name

    class Meta:
        verbose_name = 'Table Price'
        verbose_name_plural = 'Table Prices'
