from django.urls import path
from .views import  TodoDetailAPIView

urlpatterns = [
    path('data/<int:pk>', TodoDetailAPIView.as_view(), name='todo-detail')
]