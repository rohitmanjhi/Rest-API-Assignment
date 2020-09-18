from django.shortcuts import render
from rest_framework import filters
from .models import Inventory
from .serializer import InventorySerializer
from rest_framework import generics
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.


class InventoryListView(generics.ListAPIView):
    queryset = Inventory.objects.all()
    serializer_class = InventorySerializer
    filter_backends = [filters.OrderingFilter]
    search_fields = ['current_stock', 'product', 'color', 'size']


@api_view(['POST'])
def inventory_content_list(request):

    if request.method == 'POST':
        serializer = InventorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def drawing_king_or_club(request):

    if request.method == 'GET':
        king = 4
        club = 13
        all_cards = 52
        response_data = {
            "probality": (king+club)/all_cards
        }
        return Response(response_data, status=status.HTTP_200_OK)


@api_view(['GET'])
def drawing_black_or_non_face_card(request):

    if request.method == 'GET':
        non_face_card = 40
        black_card = 26
        all_cards = 52
        response_data = {
            "probality": (non_face_card+black_card)/all_cards
        }
        return Response(response_data, status=status.HTTP_200_OK)
