from django.contrib import admin
from .models import Items, Order, Orderitem

# Register your models here.
class ItemAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title', )}
    list_display = [
        'title',
        'price',
        'discount_price',
    ]

admin.site.register(Items, ItemAdmin)
admin.site.register(Order)
admin.site.register(Orderitem)