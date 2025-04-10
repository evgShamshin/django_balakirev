from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpRequest, HttpResponseNotFound
from .models import WebsiteApp

about = [{'title': 'BIM', 'title_url': 'https://www.arogroup.ru/bim '},
         {'title': 'IT', 'title_url': 'https://www.arogroup.ru/it'},
         {'title': 'Design', 'title_url': 'https://www.arogroup.ru/design'},
         {'title': 'Projects', 'title_url': 'https://www.arogroup.ru/projects'},
         {'title': 'Connector', 'title_url': 'connector'}, ]


def connector_page(request: HttpRequest):  # HttpResponse
    cats = WebsiteApp.objects.all()
    data = {'title': 'Набор команд',
            'about': about,
            'cats': cats}
    return render(request, 'website_app/main.html', context=data)


def connector_commands_page(request: HttpRequest, article_slug) -> HttpResponse:
    obj = get_object_or_404(WebsiteApp, article_slug=article_slug)
    return render(request, 'website_app/command.html', context={'obj': obj, 'about': about, })


def nof_found_page(request, exception) -> HttpResponseNotFound:
    return HttpResponseNotFound('<h1>Страница не найдена</h1>\n'
                                '<h3>Проверьте доступные url адреса в .urls</h3>')
