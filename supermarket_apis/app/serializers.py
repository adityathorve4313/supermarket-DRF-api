from rest_framework import serializers
from app.models import Category , Item

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ['id', 'item_name', 'price', 'Category']

class CategorySerializer(serializers.ModelSerializer):
    items = ItemSerializer(many=True, read_only=True)

    class Meta:
        model = Category
        fields = ['id', 'name', 'parent', 'items']