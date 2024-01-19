from django.urls import path
from . import views

urlpatterns = [
    path('',views.alunoView, name='aluno-lista'),
    path('alunoID/<int:id>', views.alunoIDview, name='aluno-detalhe'),
    path('contact', views.contact_view, name='contact_view'),
]
