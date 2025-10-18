from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Evento, Inscricao
from .forms import EventoForm

@login_required
def listar_eventos(request):
    eventos = Evento.objects.all()
    return render(request, 'listar_eventos.html', {'eventos': eventos})

@login_required
def criar_evento(request):
    if not request.user.is_organizador():
        messages.error(request, 'Apenas organizadores podem criar eventos.')
        return redirect('listar_eventos')
    
    if request.method == 'POST':
        form = EventoForm(request.POST)
        if form.is_valid():
            evento = form.save(commit=False)
            evento.organizador = request.user
            evento.save()
            messages.success(request, 'Evento criado com sucesso!')
            return redirect('detalhes_evento', pk=evento.pk)
    else:
        form = EventoForm()
    
    return render(request, 'criar_evento.html', {'form': form})

@login_required
def detalhes_evento(request, pk):
    evento = get_object_or_404(Evento, pk=pk)
    inscrito = False
    
    if not request.user.is_organizador():
        inscrito = Inscricao.objects.filter(
            usuario=request.user, 
            evento=evento, 
            status='CONFIRMADA'
        ).exists()
    
    inscritos = evento.inscricoes.filter(status='CONFIRMADA') if request.user.is_organizador() else None
    
    context = {
        'evento': evento,
        'inscrito': inscrito,
        'inscritos': inscritos,
        'pode_inscrever': evento.pode_inscrever(request.user) and evento.esta_aberto(),
    }
    
    context['inscricoes'] = evento.inscricoes.filter(status='CONFIRMADA') if request.user.perfil == 'ORGANIZADOR' or evento.organizador == request.user else None
    return render(request, 'detalhes_evento.html', context)

@login_required
def inscrever_evento(request, pk):
    evento = get_object_or_404(Evento, pk=pk)
    
    if request.user.is_organizador():
        messages.error(request, 'Organizadores não podem se inscrever em eventos.')
        return redirect('detalhes_evento', pk=pk)
    
    if not evento.esta_aberto():
        messages.error(request, 'Este evento não está disponível para inscrições.')
        return redirect('detalhes_evento', pk=pk)
    
    if not evento.pode_inscrever(request.user):
        messages.error(request, 'Você já está inscrito neste evento.')
        return redirect('detalhes_evento', pk=pk)
    
    Inscricao.objects.create(usuario=request.user, evento=evento)
    messages.success(request, 'Inscrição realizada com sucesso!')
    
    return redirect('detalhes_evento', pk=pk)

@login_required
def cancelar_inscricao(request, inscricao_id):
    inscricao = get_object_or_404(Inscricao, pk=inscricao_id, usuario=request.user)

    # Verificar se a inscrição pertence ao usuário logado
    if inscricao.usuario != request.user:
        messages.error(request, 'Você não tem permissão para cancelar esta inscrição.')
        return redirect('minhas_inscricoes')

    inscricao.status = 'CANCELADA'
    inscricao.save()

    messages.success(request, 'Inscrição cancelada com sucesso!')
    return redirect('minhas_inscricoes')

@login_required
def minhas_inscricoes(request):
    if request.user.is_organizador():
        messages.info(request, 'Organizadores não possuem inscrições.')
        return redirect('dashboard')
    
    inscricoes = Inscricao.objects.filter(usuario=request.user).exclude(status='CANCELADA')
    return render(request, 'minhas_inscricoes.html', {'inscricoes': inscricoes})

