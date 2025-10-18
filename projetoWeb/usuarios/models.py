from django.contrib.auth.models import AbstractUser
from django.db import models

class Usuario(AbstractUser):
    PERFIL_CHOICES = [
        ('ALUNO', 'Aluno'),
        ('PROFESSOR', 'Professor'),
        ('ORGANIZADOR', 'Organizador'),
    ]
    
    telefone = models.CharField(max_length=15)
    instituicao_ensino = models.CharField(max_length=200)
    perfil = models.CharField(max_length=20, choices=PERFIL_CHOICES)
    data_cadastro = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        db_table = 'usuario'
        verbose_name = 'Usuário'
        verbose_name_plural = 'Usuários'
    
    def __str__(self):
        return f"{self.get_full_name()} - {self.perfil}"
    
    def is_organizador(self):
        return self.perfil == 'ORGANIZADOR'
    
    def is_aluno(self):
        return self.perfil == 'ALUNO'
    
    def is_professor(self):
        return self.perfil == 'PROFESSOR'