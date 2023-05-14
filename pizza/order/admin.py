from django.contrib import admin, messages
from .models import OrderModel, OrderProxy
from django.utils.translation import ngettext

@admin.action(description='Set orders to delivered status')
def set_delivered(self, request, queryset):
    updated = queryset.update(delivery_status='DEL')
    self.message_user(request, ngettext(
        '%d order was successfully marker as delivered.',
        '%d order were successfully marker as delivered.', 
        updated,) % updated, messages.SUCCESS)

class OrderInLine(admin.TabularInline):
    model = OrderProxy
    verbose_name = 'order'
    verbose_name_plural = 'Create order'
    extra = 0

class OrderAdmin(admin.ModelAdmin):
    inlines = [
        OrderInLine,
    ]
    exclude = ('pizza_order', )
    list_display = ('address', 'time', 'all_orders', 'delivery_status')
    actions = [set_delivered]

admin.site.register(OrderModel, OrderAdmin)
