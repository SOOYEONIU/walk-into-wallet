from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
import json
from django.http import HttpResponse, HttpResponseBadRequest, JsonResponse
from .models import Income, Expense, Budget

def get_data(request) :
    incomes = list(Income.objects.values())
    expenses = list(Expense.objects.values())
    budgets = list(Budget.objects.values())
    data = {
        'incomes': incomes,
        'expenses': expenses,
        'budgets': budgets
    }
    return JsonResponse(data)

@csrf_exempt
@require_http_methods(["POST"])
def add_income(request):
    try:
        data = json.loads(request.body)
        income = Income(date=data['date'], amount=data['amount'], source=data['source'], description=data['description'])
        income.save()
        return JsonResponse({'message': 'Income added successfully'})
    except (KeyError, ValueError) as e:
        return HttpResponseBadRequest(str(e))

@csrf_exempt
@require_http_methods(["POST"])
def add_budget(request):
    try:
        data = json.loads(request.body)
        expense = Expense(date=data['date'], amount=data['amount'], category=data['category'], description=data['description'])
        expense.save()
        return JsonResponse({'message': 'Expense added successfully'})
    except (KeyError, ValueError) as e:
        return HttpResponseBadRequest(str(e))

@csrf_exempt
@require_http_methods(["POST"])
def add_expense(request):
    try:
        data = json.loads(request.body)
        budget = Budget(month=data['month'], income_goal=data['income_goal'], expense_limit=data['expense_limit'])
        budget.save()
        return JsonResponse({'message': 'Budget added successfully'})
    except (KeyError, ValueError) as e :
        return HttpResponseBadRequest(str(e))
