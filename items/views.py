from .serializers import *
from rest_framework.views import APIView
from .models import *
from rest_framework.response import Response
from rest_framework import status

class ItemView(APIView):
    serializer_class = ItemSerializer

    def get(self, request, id=None):
        if id:
            item = Item.objects.get(id=id)
            serializer = ItemSerializer(item)
            print(serializer.data)
        else:
            items = Item.objects.all()
            serializer = ItemSerializer(items, many=True)

        return Response(data=serializer.data, status=status.HTTP_200_OK)