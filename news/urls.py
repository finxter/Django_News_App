from django.urls import path
from .views import news_lists

urlpatterns = [
    path('', news_lists, name='home'),
]
