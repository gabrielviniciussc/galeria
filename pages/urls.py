from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Página inicial
    path('about/', views.about, name='about'),  # Página sobre
]
