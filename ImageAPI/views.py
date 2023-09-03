from django.shortcuts import render
from django.core.files.storage import default_storage

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


def prediction(request):
    
    Image_data = Image.objects.last()

    file_url = default_storage.url(Image_data.image)

    testimage = '.'+file_url

    img_height, img_width = 224, 224
    img = image.load_img(testimage, target_size=(img_height, img_width))
    x = image.img_to_array(img)
    x = x / 255.0
    x = x.reshape(1, img_height, img_width, 3)

    with model_graph.as_default():
        with tf_session.as_default():
            global predi
            predi = model.predict(x)
            
    
    predictedLabel = labelInfo[str(np.argmax(predi[0]))]
    
    top_five = {}

    for i in range(5):
        predictedLabel2 = labelInfo[str(np.argmax(predi[0][i:]))]
        chances = (sum(predi[0][i:])/sum(predi[0]))*100
        top_five[predictedLabel2[1]] = chances
    
    return render(request, 'ImageAPI/prediction.html', {"file_path": file_url, "predictedLabel": predictedLabel[1], 
                                               'top_five': top_five})


