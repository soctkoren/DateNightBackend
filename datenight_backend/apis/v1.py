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

def upload_date_hero_img(request):
    user_id = request.POST.get('user_id')
    date_img = request.FILES['date_img']
    date_id = request.POST.get('date_id')
    response = create_date_hero_img(date_img, user_id, date_id)
    return JsonResponse(response)

def node(request):
    date_id = request.POST.get('date_id')
    order_number = request.POST.get('order_num')
    node_type = request.POST.get('node_type')
    address = request.POST.get('address')
    user_id = request.POST.get('user_id')
    is_hidden = False
    response = create_node(date_id, order_number, node_type, is_hidden, address, user_id)
    return JsonResponse(response)

def date(request):
    date_id = request.GET.get('date_id', '')
    date = get_date(date_id)
    user_date = get_user_id_from_date(date_id)
    response = {}
    response['date'] = date.create_payload()
    response['user_id'] = user_date.user_id
    return JsonResponse(response)
