from django.shortcuts import render
from menu.models import Restaurant, Menu
from django.http import JsonResponse
def index(request):
    model = Restaurant
    template_name = 'name'
    restaurant = Restaurant.objects.get(name='McDonalds')
    context = {}
    context['restaurant'] = Restaurant.objects.get(name='McDonalds')
    context['menu'] = Menu.objects.get(restaurant=restaurant)
    return render(request, 'index.html', context=context)


def updateItem(request):
    return JsonResponse('Item was added', safe = False)