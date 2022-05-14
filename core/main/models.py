from django.db import models

# Create your models here.


class Food(models.Model):
    name = models.CharField('Food name', max_length=200)
    about = models.TextField('Food about')
    img = models.ImageField('Food img', upload_to='media')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Food'
        verbose_name_plural = 'Foods'