from django.db import models

# Create your models here.
class Curso(models.Model):
    codigo = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=200, null=False)
    valor = models.DecimalField(max_length=11, max_digits=11, decimal_places=2, null=False)
    def __str__(self):
        return self.nome

class Turma(models.Model):
    curso = models.ForeignKey(Curso, on_delete=models.DO_NOTHING)
    dataInicio = models.DateTimeField(null=False)
    dataTermino = models.DateTimeField(null=False)
    def __str__(self):
        return f"{self.curso.nome} - {self.dataInicio} - {self.dataTermino}"

class Professor(models.Model):
    nome = models.CharField(max_length=100, null=False)
    email = models.CharField(max_length=100, null=False)
    telefone = models.CharField(max_length=25, null=False)
    def __str__(self):
        return f"{self.nome} - {self.email} - {self.telefone}"

class Aluno(models.Model):
    nome = models.CharField(max_length=100, null=False)
    dataNascimento = models.DateField(null=False)
    endereco = models.CharField(max_length=200, null=False)
    email = models.CharField(max_length=100, null=False)
    telefone = models.CharField(max_length=25, null=False)
    def __str__(self):
        return f"{self.nome} - {self.dataNascimento} - {self.endereco} - {self.email} - {self.telefone}"
