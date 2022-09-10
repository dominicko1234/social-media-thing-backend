from .views import main
from django.urls import path, include
from .views import *

urlpatterns = [
    path('group/', GroupView.as_view()),
    path('group_messages/', GroupMessagesView.as_view())
]