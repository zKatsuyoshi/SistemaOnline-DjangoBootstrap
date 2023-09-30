from django.http import HttpResponse
from django.shortcuts import render, redirect

from Cadastro.forms import CursoForm, ProfessorForm, AlunoForm
from Cadastro.models import Curso, Professor, Aluno


def index(request):
    return render(request, template_name="inicio.html")

def listarCursos(request):
    cursos = Curso.objects.all().order_by('-nome')
    return render(request, template_name="listar_cursos.html", context={'lista': cursos})

def incluirCursos(request):
    if request.method == 'POST':
        form = CursoForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                model = form.instance
                return redirect('listar_cursos')
            except:
                pass
    else:
        form = CursoForm()
    return render(request, template_name="incluir_cursos.html", context={'form': form})

def editarCursos(request, id):
    curso = Curso.objects.get(codigo=id)
    form = CursoForm(instance=curso)
    if request.method == 'POST':
        form = CursoForm(request.POST, instance=curso)
        if form.is_valid():
            try:
                form.save()
                return redirect('listar_cursos')
            except:
                pass
    return render(request, template_name="incluir_cursos.html", context={'form': form})

def excluir_cursos(request, id):
    curso = Curso.objects.get(codigo=id)
    try:
        curso.delete()
    except:
        pass
    return redirect('listar_cursos')

def listarProfessores(request):
    professor = Professor.objects.all().order_by('-nome')
    return render(request, template_name="listarProfessores.html", context={'lista': professor})

def incluirProfessores(request):
    if request.method == 'POST':
        form = ProfessorForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                model = form.instance
                return redirect('listarProfessores')
            except:
                pass
    else:
        form = ProfessorForm()
    return render(request, template_name="incluirProfessores.html", context={'form': form})

def editarProfessores(request, id):
    professor = Professor.objects.get(id=id)
    form = ProfessorForm(instance=professor)
    if request.method == 'POST':
        form = ProfessorForm(request.POST, instance=professor)
        if form.is_valid():
            try:
                form.save()
                return redirect('listarProfessores')
            except:
                pass
    return render(request, template_name="incluirProfessores.html", context={'form': form})

def excluirProfessores(request, id):
    professor = Professor.objects.get(id=id)
    try:
        professor.delete()
    except:
        pass
    return redirect('listarProfessores')

def listarAlunos(request):
    aluno = Aluno.objects.all().order_by('-nome')
    return render(request, template_name="listarAlunos.html", context={'lista': aluno})

def incluirAlunos(request):
    if request.method == 'POST':
        form = AlunoForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                model = form.instance
                return redirect('listarAlunos')
            except:
                pass
    else:
        form = AlunoForm()
    return render(request, template_name="incluirAlunos.html", context={'form': form})

def editarAlunos(request, id):
    aluno = Aluno.objects.get(id=id)
    form = AlunoForm(instance=aluno)
    if request.method == 'POST':
        form = AlunoForm(request.POST, instance=aluno)
        if form.is_valid():
            try:
                form.save()
                return redirect('listarAlunos')
            except:
                pass
    return render(request, template_name="incluirAlunos.html", context={'form': form})

def excluirAlunos(request, id):
    aluno = Aluno.objects.get(id=id)
    try:
        aluno.delete()
    except:
        pass
    return redirect('listarAlunos')
