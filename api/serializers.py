from rest_framework import serializers
from .models import Category, Food_image, Food, Department


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class FoodImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Food_image
        fields = '__all__'


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = '__all__'


class FoodSerializer(serializers.ModelSerializer):
    image_url = FoodImageSerializer(many=True, read_only=True)
    category = CategorySerializer()
    department = DepartmentSerializer(many=True, read_only=True)

    class Meta:
        model = Food
        fields = '__all__'
