from django.urls import path
from .views import APIShortenURL, APIExpandURL

urlpatterns = [
    path('shorten/', APIShortenURL.as_view(), name='api_shorten'),
    path('<str:short_code>/', APIExpandURL.as_view(), name='api_expand'),
]
