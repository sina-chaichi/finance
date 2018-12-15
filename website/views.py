from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from json import JSONEncoder
from .models import Expense, Income, Token, User
from datetime import datetime
# Create your views here.


# TODO: validate data

@csrf_exempt
def submit_expense(request):
    """ user submit an expense"""
    this_token = request.POST['token']
    this_user = User.objects.filter(token__token = this_token).get()
    if 'date' not in request.POST:
        date = datetime.now()
    else:
        date = request.POST['date']
    Expense.objects.create(user = this_user, amount = request.POST['amount'],
        text = request.POST['text'], date = date)
    print(request.POST)
    return JsonResponse({
    'status':'ok'},
    encoder=JSONEncoder)



@csrf_exempt
def submit_income(request):
    """ user submit an income"""
    this_token = request.POST['token']
    this_user = User.objects.filter(token__token = this_token).get()
    if 'date' not in request.POST:
        date = datetime.now()
    else:
        date = request.POST['date']
    Income.objects.create(user = this_user, amount = request.POST['amount'],
        text = request.POST['text'], date = date)
    print(request.POST)
    return JsonResponse({
    'status':'ok'},
    encoder=JSONEncoder)
