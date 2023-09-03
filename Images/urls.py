from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView
from ImageAPI import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='ImageAPI/index.html')),
    path('api/', include('ImageAPI.urls', namespace='ImageAPI')),
    path('prediction/', views.prediction, name='prediction')
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)