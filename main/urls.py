from django.urls import path
from . import views
from .views import AlunoUpdateView

urlpatterns = [
    path('',views.alunoView, name='aluno-lista'),
    path('alunoID/<int:id>', views.alunoIDview, name='aluno-detalhe'),
    path('contact', views.contact_view, name='contact_view'),
    path('aluno/create/', views.aluno_create_view, name='aluno-create'),
    path('aluno/<int:pk>/update/', AlunoUpdateView.as_view(), name='aluno-update'),
]
