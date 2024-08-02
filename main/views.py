from .models import Aluno
from .forms import AlunoForm
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse,reverse_lazy
from django.views.generic.edit import UpdateView


def alunoView(request):
    alunos_list = Aluno.objects.all()
    return render(request, 'main/alunos.html', {'alunos_list': alunos_list})


def alunoIDview(request, id):
    aluno = get_object_or_404(Aluno, pk=id)
    print(aluno)
    return render(request, 'main/alunoID.html', {'aluno':aluno})


