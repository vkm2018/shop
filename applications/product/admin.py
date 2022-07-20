from django.contrib import admin

# Register your models here.
from applications.product.models import Category, Product, Image

admin.site.register(Category)
# admin.site.register(Product)
admin.site.register(Image)


class ImageInAdmin(admin.TabularInline):
    model = Image
    fields = ['image']
    max_num = 5


class ProductAdmin(admin.ModelAdmin):
    inlines = [ImageInAdmin]


admin.site.register(Product, ProductAdmin)
