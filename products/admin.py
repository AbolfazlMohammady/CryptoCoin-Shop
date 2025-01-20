from django.contrib import admin
from django.urls import path
from django.http import HttpResponse
from django.template import loader
from .models import Product, Order
from import_export.admin import ExportMixin, ImportMixin


def product_chart_view(request):
    products = Product.objects.all()
    template = loader.get_template('admin/product_chart.html')
    context = {
        'products': products,
    }
    return HttpResponse(template.render(context, request))

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock', 'created_at', 'updated_at')
    search_fields = ('name', 'description')
    change_list_template = "admin/product_change_list.html"

    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path('product-chart/', self.admin_site.admin_view(product_chart_view), name='product-chart'),
        ]
        return custom_urls + urls

@admin.register(Order)
class OrderAdmin(ExportMixin, ImportMixin,admin.ModelAdmin):
    list_display = ('id', 'user', 'product', 'quantity', 'total_price', 'created_at', 'updated_at')
    list_filter = ('created_at', 'updated_at')
    search_fields = ('user__username', 'product__name')
