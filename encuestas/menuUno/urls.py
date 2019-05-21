from django.urls import path, include

from . import views

app_name = 'menuUno'
urlpatterns = [
    # path('', views.nota_lista, name='nota_list'),
    path('listaClientes', views.persona_lista, name='persona_list'),
    path('listaNotas', views.nota_lista, name='nota_list'),
    path('<int:persona_pk>/<int:nota_pk>', views.nota_detail, name='nota_detail'),
    path('<int:pk>/', views.persona_detail, name='persona_detail'),
    path('<int:pk>/', views.nota_detail, name='nota_detail'),
    path('createPersona/', views.persona_create_view, name='persona_create'),
    path('createNota/', views.nota_create_view, name='nota_create'),

]