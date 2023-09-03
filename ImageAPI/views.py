from django.shortcuts import render
from rest_framework import generics
from ImageAPI.models import Image
from .serializers import ImageSerializer

from keras.preprocessing import image
from keras.models import load_model
import tensorflow as tf

import numpy as np
import json
import math

class ImageListView(generics.ListCreateAPIView):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer

class ImageDetailView(generics.RetrieveDestroyAPIView):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer


with open('./models/imagenet_classes.json', 'r') as f:
    labelInfo = f.read()

labelInfo = json.loads(labelInfo)


model_graph = tf.Graph()
with model_graph.as_default():
    tf_session = tf.compat.v1.Session()
    with tf_session.as_default():
        model = load_model('./models/MobileNetModelImagenet.h5') 