from django.db import models

# Create your models here.
class ProductCategory(models.Model):
    name = models.CharField(max_length=64, blank=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Категория товара"
        verbose_name_plural = "Категория товаров"

    def __str__(self):
        return '%s' % self.name

class Product(models.Model):
    name = models.CharField(max_length=64)
    is_active = models.BooleanField(default=True)
    price = models.DecimalField(default=0, max_digits=10, decimal_places=2)
    discount = models.IntegerField(default=0, blank=True)
    category = models.ForeignKey(ProductCategory, blank=True, null=True,default=None)
    short_description = models.TextField(blank=True, null=True, default=None)
    description = models.TextField(blank=True, null=True, default=None)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"

    def __str__(self):
        return '%s, %s' % (self.price, self.name)



class ProductImage(models.Model):
    product = models.ForeignKey(Product, blank=True, null=True, default=None)
    image = models.ImageField(upload_to='products_images/')
    is_main = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    class Meta:
        verbose_name = "Фотография"
        verbose_name_plural = "Фотографии"

    def __str__(self):
        return '%s' % (self.product.name)