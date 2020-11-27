from django.shortcuts import render
from menu.models import Restaurant, Menu, Order, Customer, Product
from django.http import JsonResponse
from .utils import cookieCart, cartData, guestOrder
import json

def index(request):
    model = Restaurant
    template_name = 'name'
    restaurant = Restaurant.objects.get(name='McDonalds')
    context = {}
    context['restaurant'] = Restaurant.objects.get(name='McDonalds')
    context['menu'] = Menu.objects.get(restaurant=restaurant)
    return render(request, 'index.html', context=context)


def updateItem(request):
    data = json.loads(request.body)
    productId =  data['productId']
    action =  data['action']
    user = request.user
    #customer = request.user.customer    
    product = Product.objects.get(id=productId)

    print("Action:", action)
    print("User", user)
    print("ProductId", productId)
    #order, created = Order.objects.get_or_create(customer = customer, complete=False)
    return JsonResponse('Item was added', safe = False)