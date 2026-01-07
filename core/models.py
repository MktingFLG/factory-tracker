from django.db import models

class Factory(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=100)
    sku = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class Inventory(models.Model):
    factory = models.ForeignKey(Factory, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)

    class Meta:
        unique_together = ("factory", "product")


class ProductionLog(models.Model):
    factory = models.ForeignKey(Factory, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity_produced = models.IntegerField()
    timestamp = models.DateTimeField(auto_now_add=True)
