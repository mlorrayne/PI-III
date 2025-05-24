from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index, name='index'),
    path('historia/', views.historia, name='historia'),
    path('contato/', views.contato, name='contato'),
    path('apoio/', views.apoio, name='apoio'),
    path('voluntariado/', views.voluntariado, name='voluntariado'),
    path('voluntariado/sucesso/', views.voluntariado_sucesso, name='voluntariado_sucesso'),
    path('apoio/agradecimento/', views.apoio_agradecimento, name='apoio_agradecimento'),
    path('admin/voluntariados/', views.lista_voluntariados, name='lista_voluntariados'),
    path('admin/apoios/', views.lista_apoios, name='lista_apoios'),
    path('login/', auth_views.LoginView.as_view(template_name='core/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='index'), name='logout'),

]
