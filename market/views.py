from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render

from .modules.api_storage_module.api_storage_module import ApiStorageModule
from .modules.api_storage_module.schemas.user_schema import UserSignUpRequestSchema

api_storage_module = ApiStorageModule('https://admin.stopdrugsbot.in.ua/')


def index(request):
    access_token = api_storage_module.sing_in(UserSignUpRequestSchema(
        id=760512788,
        first_name="lev",
        last_name="zharov",
        username="laddon",
    ))
    links = api_storage_module.get_link(access_token)
    return render(request, 'market/index.html', {'title': 'Main page', 'links': links})


def pageNotFound(request, exception):
    return render(request, 'market/404.html', {'title': '404 Error Page'})


def market(request):
    access_token = api_storage_module.sing_in(UserSignUpRequestSchema(
        id=760512788,
        first_name="lev",
        last_name="zharov",
        username="laddon",
    ))
    return HttpResponse(api_storage_module.get_link(access_token))


