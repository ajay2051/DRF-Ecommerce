from django.shortcuts import render
from rest_framework import viewsets
from drf_spectacular.utils import extend_schema
from rest_framework.response import Response

from .models import Category
from .serializers import BrandSerializer, CategorySerializer, ProductSerializer


class CategoryView(viewsets.ViewSet):
    """A simple viewlet for viewing all categories"""
    queryset = Category.objects.all()

    @extend_schema(responses=CategorySerializer)
    def list(self, request):
        serializer = CategorySerializer(self.queryset, many=True)
        return Response(serializer.data)


class BrandView(viewsets.ViewSet):
    """A simple viewlet for viewing all brands"""
    queryset = BrandSerializer.Meta.model.objects.all()

    @extend_schema(responses=BrandSerializer)
    def list(self, request):
        serializer = BrandSerializer(self.queryset, many=True)
        return Response(serializer.data)


class ProductView(viewsets.ViewSet):
    """A simple viewlet for viewing all brands"""
    queryset = ProductSerializer.Meta.model.objects.all()

    @extend_schema(responses=ProductSerializer)
    def list(self, request):
        serializer = ProductSerializer(self.queryset, many=True)
        return Response(serializer.data)
