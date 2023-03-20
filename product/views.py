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
