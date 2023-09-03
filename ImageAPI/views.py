from django.shortcuts import render
from rest_framework import generics
from ImageAPI.models import Image
from .serializers import ImageSerializer

class ImageListView(generics.ListCreateAPIView):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer