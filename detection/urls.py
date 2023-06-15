from django.urls import path
from .views import detect_cancer

urlpatterns = [
    path('detect-cancer/', detect_cancer, name='detect-cancer'),
    # Other URL patterns for your project...
]

