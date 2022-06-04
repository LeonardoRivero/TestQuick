from .models import Bills, Products, Clients
from rest_framework import serializers


class BillsSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        products = validated_data.pop('products')
        instance = Bills.objects.create(**validated_data)
        for product in products:
            instance.products.add(product)
        return instance

    class Meta:
        model = Bills
        fields = ["id", "client_id", "company_name", "nit", "code", "products"]


class RelationBillsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bills
        fields = ["id", "client_id", "company_name", "nit", "code", "products"]
        depth = 3


class ProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = ["id", "name", "description", "attribute"]


class RelationProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = ["id", "name", "description", "attribute"]
        depth = 3


class ClientsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clients
        fields = ["id", "document", "first_name", "last_name", "email"]


class RelationClientsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clients
        fields = ["id", "document", "first_name", "last_name", "email"]
        depth = 3
