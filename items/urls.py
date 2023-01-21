from django.urls import path, include
from .views import *
urlpatterns = [
    path('items/',ItemView.as_view(),name='items')
]