from django.urls import path
from .views import factory_list, product_list, inventory_list, log_production

urlpatterns = [
    path("factories/", factory_list),
    path("products/", product_list),
    path("inventory/", inventory_list),
    path("production/", log_production),
]
