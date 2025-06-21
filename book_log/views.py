from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


from .models import Book,Category
from .serializers import BookSerializer, CategorySerializer

import json



@api_view(['GET'])
def get_books(request):

    if request.method == 'GET':

        books = Book.objects.all()

        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)
    
    return Response(status=status.HTTP_400_BAD_REQUEST)