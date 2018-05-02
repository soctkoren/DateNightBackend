from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from datenight_backend.workers.date_creation import *
from django.template import loader

from datenight_backend.models.date import Date
from django.middleware.csrf import get_token

def index(request):
    # csrf_token = get_token(request)
    template = loader.get_template('create_dates/index.html')
    context = {}
    return HttpResponse(template.render(context, request))

def initialize_create_flow(request):
    user_id = request.POST.get('user_id')
    response = {}
    response['date_id'] = create_draft(user_id)
    response['user_id'] = user_id
    return JsonResponse(response)

def upload_img(request):
    user_id = request.POST.get('user_id')
    date_img = request.POST.get('date_img')
    response = create_img(date_img, user_id)
    return JsonResponse(response)

def date(request):
    date_id = request.GET.get('date_id', '')
    date = get_date(date_id)
    user_date = get_user_id_from_date(date_id)
    response = {}
    response['date'] = date.create_payload()
    response['user_id'] = user_date.user_id
    return JsonResponse(response)
