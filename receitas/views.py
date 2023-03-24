from django.shortcuts import render

from receitas.models import Receita

# from .utils.receitas.factory import make_recipe


def home(request):
    receitas = Receita.objects.filter(is_published=True).order_by('-id')
    return render(request, 'receitas/pages/home.html', context={
        'receitas': receitas
    })


def category(request, category_id):
    receitas = Receita.objects.filter(
        category__id=category_id, is_published=True).order_by('-id')
    return render(request, 'receitas/pages/category.html', context={
        'receitas': receitas
    })


def receitas(request, id):
    receita = Receita.objects.get(id=id)
    return render(request, 'receitas/pages/receitas-views.html', context={
        'receita': receita,
        'is_detail_page': True
    })
