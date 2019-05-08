from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.encusta_lista),
    path('<int:pk>/', views.encuesta_detail),
]