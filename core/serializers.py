from rest_framework import serializers
from .models import Factory, Product, Inventory, ProductionLog


class FactorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Factory
        fields = "__all__"


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"


class InventorySerializer(serializers.ModelSerializer):
    factory = FactorySerializer(read_only=True)
    product = ProductSerializer(read_only=True)

    class Meta:
        model = Inventory
        fields = "__all__"


class ProductionLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductionLog
        fields = "__all__"
