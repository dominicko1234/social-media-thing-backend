from .views import main
from django.urls import path, include
from .views import *

urlpatterns = [
    path('', GroupView.as_view())
]