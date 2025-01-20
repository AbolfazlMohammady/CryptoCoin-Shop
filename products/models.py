from django.db import models
from django.conf import settings

class Product(models.Model):
    name = models.CharField(max_length=255, verbose_name="نام", null=True, blank=True)
    description = models.TextField(verbose_name="توضیحات", null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="قیمت", null=True, blank=True)
    stock = models.IntegerField(verbose_name="موجودی", null=True, blank=True)
    image = models.ImageField(upload_to='product_images/', null=True, blank=True, verbose_name="تصویر")
    weight = models.DecimalField(max_digits=5, decimal_places=2, help_text="وزن به گرم", verbose_name="وزن", null=True, blank=True)
    dimensions = models.CharField(max_length=50, help_text="ابعاد به میلیمتر (طول*عرض*ارتفاع)", verbose_name="ابعاد", null=True, blank=True)
    thickness = models.DecimalField(max_digits=5, decimal_places=3, help_text="ضخامت به میلیمتر", verbose_name="ضخامت", null=True, blank=True)
    certificate_dimensions = models.CharField(max_length=50, help_text="ابعاد شناسنامه به میلیمتر (طول*عرض)", verbose_name="ابعاد شناسنامه", null=True, blank=True)
    certificate_type = models.CharField(max_length=255, help_text="نوع شناسنامه", verbose_name="نوع شناسنامه", null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="تاریخ ایجاد", null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, verbose_name="تاریخ بروزرسانی", null=True, blank=True)

    def __str__(self):
        return self.name


class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Order {self.id} by {self.user.username}'