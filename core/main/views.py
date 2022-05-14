from django.shortcuts import render
from .models import Food
# Create your views here.

def food(request):
    food_list = Food.objects.all()
    context = {
        'food_list':food_list
    }
    return render(request, 'food.html', context)

def about(request):
    return render(request, 'about.html')