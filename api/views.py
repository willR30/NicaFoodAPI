from django.shortcuts import render
from rest_framework import viewsets
from .models import Category, Food_image, Food
from .serializers import CategorySerializer, FoodImageSerializer, FoodSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class FoodImageViewSet(viewsets.ModelViewSet):
    queryset = Food_image.objects.all()
    serializer_class = FoodImageSerializer


class FoodViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Food.objects.all()
    serializer_class = FoodSerializer


def index(request):
    return render(request, 'index.html')




