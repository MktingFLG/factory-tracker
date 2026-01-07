from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import Factory, Product, Inventory, ProductionLog
from .serializers import (
    FactorySerializer,
    ProductSerializer,
    InventorySerializer,
    ProductionLogSerializer,
)


@api_view(["GET"])
def factory_list(request):
    factories = Factory.objects.all()
    serializer = FactorySerializer(factories, many=True)
    return Response(serializer.data)


@api_view(["GET"])
def product_list(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)


@api_view(["GET"])
def inventory_list(request):
    inventory = Inventory.objects.select_related("factory", "product")
    serializer = InventorySerializer(inventory, many=True)
    return Response(serializer.data)


@api_view(["POST"])
def log_production(request):
    serializer = ProductionLogSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
