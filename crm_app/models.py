from django.db import models


class OrderStatus(models.Model):
    status_name = models.CharField(max_length=50, verbose_name='Order Status')

    def __str__(self):
        return self.status_name

    class Meta:
        verbose_name = 'Status'
        verbose_name_plural = 'Statuses'


class Order(models.Model):
    order_dt = models.DateTimeField(auto_now=True)
    order_name = models.CharField(max_length=100, verbose_name='Name')
    order_phone = models.CharField(max_length=50, verbose_name='Phone')
    order_status = models.ForeignKey(OrderStatus, on_delete=models.PROTECT, null=True, blank=True)

    def __str__(self):
        return f'Order #{self.pk} from {str(self.order_dt)[:19]}'

    class Meta:
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'


class OrderComment(models.Model):
    comment_binding = models.ForeignKey(Order, on_delete=models.CASCADE, verbose_name='Order')
    comment_text = models.TextField(verbose_name='Comment Text')
    comment_dt = models.DateTimeField(auto_now=True, verbose_name='Time of comment creation')

    def __str__(self):
        return self.comment_text

    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'
