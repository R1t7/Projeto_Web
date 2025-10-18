from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone

Usuario = get_user_model()

class Evento(models.Model):
    TIPO_CHOICES = [
        ('SEMINARIO', 'Seminário'),
        ('PALESTRA', 'Palestra'),
        ('MINICURSO', 'Minicurso'),
        ('SEMANA_ACADEMICA', 'Semana Acadêmica'),
    ]
    
    STATUS_CHOICES = [
        ('ABERTO', 'Aberto'),
        ('FECHADO', 'Fechado'),
        ('CANCELADO', 'Cancelado'),
    ]
    
    tipo = models.CharField(max_length=20, choices=TIPO_CHOICES)
    titulo = models.CharField(max_length=200)
    descricao = models.TextField()
    data_inicio = models.DateField()
    data_fim = models.DateField()
    horario = models.TimeField()
    local = models.CharField(max_length=200)
    vagas = models.IntegerField()
    organizador = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='eventos_organizados')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='ABERTO')
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'evento'
        verbose_name = 'Evento'
        verbose_name_plural = 'Eventos'
        ordering = ['-data_inicio']

    def __str__(self):
        return f"{self.titulo} - {self.get_tipo_display()}"

    @property
    def vagas_disponiveis(self):
        inscritos = self.inscricoes.filter(status='CONFIRMADA').count()
        return self.vagas - inscritos
    
    def esta_aberto(self):
        return self.status == 'ABERTO' and self.vagas_disponiveis > 0
    
    def pode_inscrever(self, usuario):
        if usuario.is_organizador():
            return False
        return not self.inscricoes.filter(usuario=usuario, status='CONFIRMADA').exists()

class Inscricao(models.Model):
    STATUS_CHOICES = [
        ('CONFIRMADA', 'Confirmada'),
        ('CANCELADA', 'Cancelada'),
    ]
    
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='inscricoes')
    evento = models.ForeignKey(Evento, on_delete=models.CASCADE, related_name='inscricoes')
    data_inscricao = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='CONFIRMADA')
    
    class Meta:
        db_table = 'inscricao'
        verbose_name = 'Inscrição'
        verbose_name_plural = 'Inscrições'
        unique_together = ('usuario', 'evento')
    
    def __str__(self):
        return f"{self.usuario.get_full_name()} - {self.evento.titulo}"

