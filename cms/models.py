from django.db import models

class Slider(models.Model):
    slider_img = models.ImageField(upload_to='sliderdir/')
    slider_name = models.CharField(max_length=50, verbose_name='Slider name')
    slider_text = models.CharField(max_length=50, verbose_name='Slider text')
    slider_css_class = models.CharField(max_length=50, null=True, default='-', verbose_name='CCS class')

    def __str__(self):
        return f'Slider {self.slider_name}'

    class Meta:
        verbose_name = 'Slider'
        verbose_name_plural = 'Sliders'