from django.contrib import admin
from .models import Factory, Product, Inventory, ProductionLog

admin.site.register(Factory)
admin.site.register(Product)
admin.site.register(Inventory)
admin.site.register(ProductionLog)
