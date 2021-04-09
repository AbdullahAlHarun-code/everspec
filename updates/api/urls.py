from django.urls import path, include
from updates.api.views import UpdateModelDetailAPIView, UpdateModelListAPIView
urlpatterns = [
    path('', UpdateModelListAPIView.as_view()),
    path('<id>/', UpdateModelDetailAPIView.as_view()),
]