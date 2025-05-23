from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('historia/', views.historia, name='historia'),
    path('contato/', views.contato, name='contato'),
]
