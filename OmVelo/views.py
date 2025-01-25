from django.shortcuts import render
from core.models import SubscriptionPlan

def home(request):
    return render(request, 'home.html')

def list_plans(request):
    subscription_plans = SubscriptionPlan.objects.all()
    return render(request, 'subs.html', {'subs_plans':subscription_plans})
