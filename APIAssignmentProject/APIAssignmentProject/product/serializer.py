from rest_framework import serializers
from APIAssignmentProject.product.models import Color, Size, Product, Inventory


class ColorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Color
        fields = ('id', 'name')


class SizeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Size
        fields = ('id', 'name')


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ('id', 'name')


class InventorySerializer(serializers.ModelSerializer):
    color = serializers.SlugRelatedField(
        queryset=Color.objects.all(), slug_field='name'
    )
    size = serializers.SlugRelatedField(
        queryset=Size.objects.all(), slug_field='name'
    )
    product = serializers.SlugRelatedField(
        queryset=Product.objects.all(), slug_field='name'
    )

    class Meta:
        model = Inventory
        fields = ('id', 'color', 'size', 'product', 'current_stock')
