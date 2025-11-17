from django.urls import path
from .views import ChatQueryView, FileUploadView, HealthCheckView

urlpatterns = [
    path('query/', ChatQueryView.as_view(), name='chat-query'),
    path('upload/', FileUploadView.as_view(), name='file-upload'),
    path('health/', HealthCheckView.as_view(), name='health-check'),
]
