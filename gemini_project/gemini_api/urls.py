from django.urls import path
from .views import GeminiAPIView

urlpatterns = [
    path('ask/', GeminiAPIView.as_view(), name='gemini-api'),
]