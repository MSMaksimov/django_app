from django.contrib import admin

from .models import Product, Order


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = "pk", "name", "description_short", "price", "discount"
    list_display_links = "pk", "name"
    ordering = "name", "pk"
    search_fields = "name", "description", "price", "discount"

    def description_short(self, obj: Product) -> str:
        if len(obj.description) < 48:
            return obj.description
        return obj.description[:48] + "..."

# admin.site.register(Product, ProductAdmin)


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = "delivery_address", "promocode", "created_at", "user"

    def get_queryset(self, request):
        return Order.objects.select_related("user")
    #
    # def user_verbose(self, obj: Order) -> str:
    #     return obj.user.f