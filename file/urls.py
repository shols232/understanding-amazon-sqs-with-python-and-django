from django.urls import path
from .views import FileView


urlpatterns = [
    path('process', FileView.as_view())
]
