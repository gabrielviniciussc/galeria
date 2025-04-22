from django.contrib import admin
from django.urls import path
from MaravilhasMundo import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),  # <-- Adicionando o nome 'index' para a página principal
    path('sobre/', views.index2, name='sobre'),  # <-- Nome necessário para {% url 'sobre' %}
]
