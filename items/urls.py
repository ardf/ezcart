from django.urls import path, include
from .views import *
urlpatterns = [
    path('items/',ItemView.as_view(),name='items'),
    path('items/<int:id>',ItemView.as_view(),name='item-detail')
]