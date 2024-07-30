from django.urls import path
from . import views
from .views import AlunoUpdateView

urlpatterns = [
    path('',views.alunoView, name='aluno-lista'),
]
