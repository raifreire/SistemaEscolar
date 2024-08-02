from django.urls import path
from . import views
#from .views import AlunoUpdateView,AlunoCreateView

urlpatterns = [
    path('',views.alunoView, name='aluno-lista'),
    path('alunoID/<int:id>', views.alunoIDview, name='aluno-detalhe'),
]
