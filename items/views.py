from .serializers import *
from rest_framework.views import APIView
from .models import *
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
class ItemView(APIView):
    serializer_class = ItemSerializer

    def get(self, request, id=None):
        if id:
            item = get_object_or_404(Item, id=id)
            serializer = ItemSerializer(item)
            print(serializer.data)
        else:
            query_params = request.query_params
            category = query_params.get('category')
            subcategory = query_params.get('subcategory')
            name = query_params.get('name')
            amount = query_params.get('amount')
            items = Item.objects.select_related('subcategory')
            if category:
                items = items.filter(subcategory__category__name = category)
            if subcategory:
                items = items.filter(subcategory__name = subcategory)
            if name:
                items = items.filter(name = name)
            if amount:
                items = items.filter(amount = amount)
            serializer = ItemSerializer(items, many=True)

        return Response(data=serializer.data, status=status.HTTP_200_OK)