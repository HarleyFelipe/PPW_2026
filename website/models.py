from django.db import models

class Usuario (models.Model):
    nome = models.CharField()
    cpf = models.CharField()
    gmail = models.CharField()
    senha = models.CharField()
    
class Admin (Usuario):
    None
    
class Instrutor (Usuario):
    curso = models.CharField()
     
class Aluno(Usuario):
    None

class Curso (models.Model):
    nome = models.CharField()
    data_hora = models.DateTimeField()
    
    
    