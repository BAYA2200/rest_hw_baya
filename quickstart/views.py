from django.http import JsonResponse
from django.shortcuts import render
from .models import Category, Item
from .serializers import CategorySerializer, ItemSerializer
from rest_framework.generics import ListCreateAPIView
# Create your views here.

from rest_framework.decorators import api_view
from rest_framework.generics import ListCreateAPIView
from rest_framework.generics import ListCreateAPIView
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import get_object_or_404


@api_view(['GET', 'POST'])
def item_list(request):
    if request.method == 'GET':
        items = Category.objects.all()
        serializers = ItemSerializer(items, many=True)
        return Response(serializers.data)
    if request.method == 'POST':
        serializer = ItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST', 'DELETE'])
def item_detail(request, pk):
    item = get_object_or_404(Item, pk=pk)
    if request.method == 'GET':
        serializer = ItemSerializer(item)
        return Response(serializer.data)
    if request.method == 'DELETE':
        item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    if request.method == 'PUT':
        serializer = ItemSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CategoryListCreateAPIView(ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
