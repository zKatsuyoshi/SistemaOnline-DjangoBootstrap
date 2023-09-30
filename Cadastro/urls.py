from django.urls import path
from .views import index, incluirCursos
from Cadastro import views

urlpatterns = [
    path('', views.index, name='index'),

    path('listar_cursos', views.listarCursos, name='listar_cursos'),
    path('incluir_cursos', views.incluirCursos, name='incluirCursos'),
    path('editar_cursos/<int:id>', views.editarCursos, name='editarCursos'),
    path('excluir_cursos/<int:id>', views.excluir_cursos, name='excluir_cursos'),

    path('listar_professores', views.listarProfessores, name='listarProfessores'),
    path('incluir_professores', views.incluirProfessores, name='incluirProfessores'),
    path('editar_professores/<int:id>', views.editarProfessores, name='editarProfessores'),
    path('excluir_professores/<int:id>', views.excluirProfessores, name='excluirProfessores'),

    path('listar_alunos', views.listarAlunos, name='listarAlunos'),
    path('incluir_alunos', views.incluirAlunos, name='incluirAlunos'),
    path('editar_alunos/<int:id>', views.editarAlunos, name='editarAlunos'),
    path('excluir_alunos/<int:id>', views.excluirAlunos, name='excluirAlunos'),
]
