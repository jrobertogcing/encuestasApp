from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.encusta_lista),
    path('<int:encuesta_pk>/<int:persona_pk>', views.persona_detail),
    path('<int:pk>/', views.encuesta_detail),
]