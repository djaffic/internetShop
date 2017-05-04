from django.db import models


# Create your models here.
class Subscriber(models.Model):
    email = models.EmailField()
    name = models.CharField(max_length=64)

    class Meta:
        verbose_name = "Подисчик"
        verbose_name_plural = "Подписчики"

    def __str__(self):
        return '%s %s' % (self.name, self.email)