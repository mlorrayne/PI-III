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

    # URLs para listagem dos formulários — sem 'admin/' no caminho
    path('voluntariados/', views.lista_voluntariados, name='lista_voluntariados'),
    path('apoios/', views.lista_apoios, name='lista_apoios'),

    # URLs para editar e excluir registros — também sem 'admin/'
    path('apoios/editar/<int:pk>/', views.editar_apoio, name='editar_apoio'),
    path('voluntariados/editar/<int:pk>/', views.editar_voluntariado, name='editar_voluntariado'),
    path('apoios/excluir/<int:pk>/', views.excluir_apoio, name='excluir_apoio'),
    path('voluntariados/excluir/<int:pk>/', views.excluir_voluntariado, name='excluir_voluntariado'),

    # Login e logout
    path('login/', auth_views.LoginView.as_view(template_name='core/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]
