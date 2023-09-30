from django.contrib import admin

from Cadastro.models import Curso, Turma, Professor, Aluno

# Register your models here.
admin.site.register(Curso)
admin.site.register(Turma)
admin.site.register(Professor)
admin.site.register(Aluno)
