# from django.shortcuts import render
from django.shortcuts import render


def blog(request):

    context = {
            'text': 'Olá blog',
            'title': 'Blog - '
        }

    return render(
        request,
        'blog/index.html',
        context,
    )


def exemplo(request):

    context = {
            'text': 'Olá exemplo',
            'title': 'Exemplo - '
        }

    return render(
        request,
        'blog/exemplo.html',
        context,
    )
