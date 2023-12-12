from django.shortcuts import render


def home(request):

    context = {
            'text': 'Olá home',
            'title': 'Home - '
        }

    return render(
        request,
        'home/index.html',
        context,
        )
