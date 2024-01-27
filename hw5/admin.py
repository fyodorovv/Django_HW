from django.contrib import admin
from hw5.models import Client, Order, Product


@admin.action(description="Сбросить количество в ноль")
def reset_quantity(modeladmin, request, queryset):
    queryset.update(count=0)


class ProductAdmin(admin.ModelAdmin):
    fieldsets = [
        (
            None,
            {
                'classes': ['wide'],
                'fields': ['title'],
            },
        ),
        (
            'Подробное описание',
            {
                'fields': ['description'],
            },
        ),
        (
            'Бухгалтерия',
            {
                'fields': ['price', 'count'],
            }
        ),
        (
            'Прочее',
            {
                'fields': ['image_scr'],
            }
        ),
    ]

    list_display = ['title', 'price', 'count']
    search_fields = ['title']
    search_help_text = 'Поиск по названию'
    list_filter = ['title', 'count']
    actions = [reset_quantity]


class ClientAdmin(admin.ModelAdmin):
    readonly_fields = ['register_date']
    fieldsets = [
        (
            None,
            {
                'classes': ['wide'],
                'fields': ['name'],
            },
        ),
        (
            'Контактная информация',
            {
                'classes': ['wide'],
                'fields': ['email', 'phone', 'address'],
            },
        ),
        (
            'Прочее',
            {
                'fields': ['register_date'],
            }
        ),
    ]

    list_display = ['name', 'email', 'register_date']
    search_fields = ['name']
    search_help_text = 'Поиск по имени'
    list_filter = ['name', 'register_date']


class OrderAdmin(admin.ModelAdmin):
    readonly_fields = ['order_date']
    fieldsets = [
        (
            None,
            {
                'classes': ['wide'],
                'fields': ['client'],
            },
        ),
        (
            'Подробное описание',
            {
                'fields': ['product', 'order_sum'],
            },
        ),
        (
            'Прочее',
            {
                'fields': ['order_date'],
            }
        ),
    ]

    list_display = ['client', 'order_sum', 'order_date']
    search_fields = ['client']
    search_help_text = 'Поиск по клиенту'
    list_filter = ['client']


admin.site.register(Client, ClientAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Order, OrderAdmin)
