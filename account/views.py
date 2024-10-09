from django.shortcuts import render, redirect
from .models import Usuario

def register_view(request):
    if request.method == 'POST':
        username = request.POST.get('uname')
        password = request.POST.get('psw')
        if Usuario.objects.filter(nome=username).exists():
            return render(request, 'account/index.html', {'error': 'Usuário já existe.'})
        novo_usuario = Usuario(
            nome=username,
            senha=password
        )
        novo_usuario.save()
        return redirect('menusel:form')

    return render(request, 'account/index.html')

def index(request):
    return render(request, 'account/index.html')