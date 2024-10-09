import uuid
from django.shortcuts import render, redirect
from .models import Plano

def form(request):
    return render(request, 'menuselection/form.html')

def menu(request):
    if 'session_id' not in request.session:
        request.session['session_id'] = str(uuid.uuid4())

    if request.method == "POST":
        nome_noivo = request.POST.get("nome_noivo")
        nome_noiva = request.POST.get("nome_noiva")
        data_casamento = request.POST.get("data")

        plano = Plano(
            id_usuario=request.session['session_id'],
            nome_1=nome_noivo,
            nome_2=nome_noiva,
            data=data_casamento
        )
        plano.save()

    return render(request, 'menuselection/menu.html')

def invite(request):
    decoracao_opcoes = {
        1: "Luzes",
        2: "Mesa de bolo",
        3: "Toalhas de mesa",
        4: "Cadeiras decoradas",
        5: "Arranjos de mesa",
        6: "Painéis decorativos"
    }

    buffet_opcoes = {
        1: "Entradas",
        2: "Pratos principais",
        3: "Bebidas",
        4: "Sobremesas",
        5: "Estações de comida",
        6: "Cardápio infantil"
    }

    items_cerimonia_opcoes = {
        1: "Alianças",
        2: "Tapete",
        3: "Velas",
        4: "Música",
        5: "Livro de assinaturas",
        6: "Decoração do altar"
    }

    transporte_opcoes = {
        1: "Carro dos noivos",
        2: "Ônibus para convidados",
        3: "Carro para padrinhos",
        4: "Carro de luxo",
        5: "Outros"
    }

    flores_opcoes = {
        1: "Buquê da noiva",
        2: "Flores da cerimônia",
        3: "Arranjos de mesa",
        4: "Buquê das madrinhas",
        5: "Flores para o altar",
        6: "Outros arranjos florais"
    }

    if request.method == "POST":
        decoracao = request.POST.getlist('decoracao[]')
        buffet = request.POST.getlist('buffet[]')
        items_cerimonia = request.POST.getlist('items_cerimonia[]')
        transporte = request.POST.getlist('transporte[]')
        flores = request.POST.getlist('flores[]')

        # Mapeando os IDs para os nomes usando os dicionários
        decoracao_str = ', '.join([decoracao_opcoes[int(item)] for item in decoracao if int(item) in decoracao_opcoes])
        buffet_str = ', '.join([buffet_opcoes[int(item)] for item in buffet if int(item) in buffet_opcoes])
        items_cerimonia_str = ', '.join([items_cerimonia_opcoes[int(item)] for item in items_cerimonia if int(item) in items_cerimonia_opcoes])
        transporte_str = ', '.join([transporte_opcoes[int(item)] for item in transporte if int(item) in transporte_opcoes])
        flores_str = ', '.join([flores_opcoes[int(item)] for item in flores if int(item) in flores_opcoes])

        # Criando o objeto Plano e salvando
        plano = Plano(
            id_usuario=request.session['session_id'],
            decoracao=decoracao_str,
            buffet=buffet_str,
            items_cerimonia=items_cerimonia_str,
            transporte=transporte_str,
            flores=flores_str,
        )
        plano.save()

    return render(request, 'menuselection/invite.html', {
        'decoracao': decoracao_str,
        'buffet': buffet_str,
        'items_cerimonia': items_cerimonia_str,
        'transporte': transporte_str,
        'flores': flores_str,
    })



def meus_planos(request):
    session_id = request.session.get('session_id')
    planos = Plano.objects.filter(id_usuario=session_id)
    return render(request, 'menuselection/meus_planos.html', {'planos': planos})

def review(request):
    if request.method == "POST":
        id_design = request.POST.get("invite")
        id_usuario = request.session.get('session_id')

        # Busca todos os planos para o usuário
        planos = Plano.objects.filter(id_usuario=id_usuario)
        
        # Cria um dicionário para armazenar as informações
        plano_info = {
            'noiva': '',
            'noivo': '',
            'data': '',
            'convidados': '',
            'decoracao': [],
            'buffet': [],
            'items_cerimonia': [],
            'flores': [],
            'transporte': []
        }

        for plano in planos:
            # Captura apenas a primeira linha para noiva, noivo, data e convidados
            if plano_info['noiva'] == '':
                plano_info['noiva'] = plano.nome_1
            if plano_info['noivo'] == '':
                plano_info['noivo'] = plano.nome_2
            if plano_info['data'] == '':
                plano_info['data'] = plano.data
            if plano_info['convidados'] == '':
                plano_info['convidados'] = plano.convidados
            
            # Adiciona as decorações e outros itens em listas
            plano_info['decoracao'].append(plano.decoracao)
            plano_info['buffet'].append(plano.buffet)
            plano_info['items_cerimonia'].append(plano.items_cerimonia)
            plano_info['flores'].append(plano.flores)
            plano_info['transporte'].append(plano.transporte)

        # Cria o contexto com todas as informações
        context = {
            'noiva': plano_info['noiva'],
            'noivo': plano_info['noivo'],
            'data': plano_info['data'],
            'convidados': plano_info['convidados'],
            'decoracao': ', '.join(plano_info['decoracao']),
            'buffet': ', '.join(plano_info['buffet']),
            'items_cerimonia': ', '.join(plano_info['items_cerimonia']),
            'flores': ', '.join(plano_info['flores']),
            'transporte': ', '.join(plano_info['transporte']),
        }
        
        return render(request, 'menuselection/review.html', context)

    # Se não houver um POST, você pode renderizar um template vazio ou com mensagem.
    return render(request, 'menuselection/review.html')
