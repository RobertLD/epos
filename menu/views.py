from django.shortcuts import render
from menu.models import Restaurant, Menu
def index(request):
    model = Restaurant
    template_name = 'name'
    restaurant = Restaurant.objects.get(name='McDonalds')
    context = {}
    context['restaurant'] = Restaurant.objects.get(name='McDonalds')
    context['menu'] = Menu.objects.get(restaurant=restaurant)
    return render(request, 'index.html', context=context)