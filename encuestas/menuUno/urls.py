from django.urls import path, include

from . import views

app_name = 'menuUno'
urlpatterns = [
    path('', views.encusta_lista, name='encuesta_list'),
    path('<int:encuesta_pk>/<int:persona_pk>', views.persona_detail, name='persona_detail'),
    path('<int:pk>/', views.encuesta_detail, name='encuesta_detail'),
]