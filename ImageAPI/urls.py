from django.urls import path
from . import views

app_name = 'ImageAPI'

urlpatterns = [
    path('', views.ImageListView.as_view(), name='image_list')
]
