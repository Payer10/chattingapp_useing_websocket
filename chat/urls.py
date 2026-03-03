from django.urls import path
from .views import ChatHistoryAPIView

urlpatterns = [
    path("api/chat/<str:username>/", ChatHistoryAPIView.as_view()),
]