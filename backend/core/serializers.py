from rest_framework import serializers
from .models import User, Category, Dish, Order, OrderItem, Review

# Serializer per l'utente: proteggiamo i dati sensibili
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'role'
        ]

# Serializer per le categorie
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = [
            'id',
            'name'
        ]

# Serializer per i piatti con riferimento al nome della categoria
class DishSerializer(serializers.ModelSerializer):
    category_name = serializers.ReadOnlyField(source='category.name')

    class Meta:
        model = Dish
        fields = [
            'id',
            'name',
            'description',
            'price',
            'category',
            'category_name',
            'is_active',
            'is_available'
        ]

# Serializer per i singoli elementi degli ordini (Nested)
class OrderItemSerializer(serializers.ModelSerializer):
    dish_details = DishSerializer(source='dish', read_only=True)

    class Meta:
        model = OrderItem
        fields = [
            'id',
            'dish',
            'dish_details',
            'quantity'
        ]

# Serializer principale per gli Ordini
class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True, read_only=True)
    user = UserSerializer(read_only=True)

    class Meta:
        model = Order
        fields = [
            'id',
            'user',
            'status',
            'items',
            'created_at',
            'notes'
        ]

# Serializer per le recensioni
class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = [
            'id',
            'order',
            'rating',
            'comment',
            'created_at'
        ]