from .models import restaurant
from django.http import HttpResponse
from django.core import serializers
from django.shortcuts import render
import json

def index(request):
    return HttpResponse("Hello to the Francesinhas restaurante search app!")

def getRestaurantByID(request, restaurant_id):
    restaurant_row = restaurant.objects.get(id=restaurant_id)
    context = {'name':getattr(restaurant_row, 'name'), 'id':getattr(restaurant_row, 'id'), 'address':getattr(restaurant_row, 'address'), 'city':getattr(restaurant_row, 'city'), 'country':getattr(restaurant_row, 'country'), 'phone_number':getattr(restaurant_row, 'phone_number'), 'email':getattr(restaurant_row, 'email'), 'description':getattr(restaurant_row, 'description'), 'rating_average':getattr(restaurant_row, 'rating_average')}
    return render(request, 'app/getRestaurantByID.html', context)

def getTop(request):
    top_ten_restaurants = restaurant.objects.order_by('-rating_average')[:10]
    context = []
    for r in top_ten_restaurants:
        row_dict = {'name':getattr(r, 'name'), 'id':getattr(r, 'id'), 'address':getattr(r, 'address'), 'city':getattr(r, 'city'), 'country':getattr(r, 'country'), 'phone_number':getattr(r, 'phone_number'), 'email':getattr(r, 'email'), 'description':getattr(r, 'description'), 'rating_average':getattr(r, 'rating_average')}
        context.append(row_dict)

    env = {'context':context}
    #return HttpResponse(print(env['ten']))
    #print(env)
    return render(request, 'app/top.html', env)

def updateRestaurantInfo(request,restaurant_id, url_search):
    keys_values = url_search.split('&')
    restaurant_object = restaurant.objects.get(id=id)
    if restaurant_object:
        for key_value in keys_values:
            key = key_value.split('=')[0]
            value = key_value.split('=')[1]
            if key=='name':
                restaurant_object.name=value
            elif key =='address':
                restaurant_object.address=value
            elif key =='city':
                restaurant_object.city=value
            elif key =='country':
                restaurant_object.country=value
            elif key =='phone_number':
                restaurant_object.phone_number=value
            elif key =='email':
                restaurant_object.email=value
            elif key =='website':
                restaurant_object.website=value
        restaurant_object.save()
    context = {'name':getattr(restaurant_object, 'name'), 'id':getattr(restaurant_object, 'id'), 'address':getattr(restaurant_object, 'address'), 'city':getattr(restaurant_object, 'city'), 'country':getattr(restaurant_object, 'country'), 'phone_number':getattr(restaurant_object, 'phone_number'), 'email':getattr(restaurant_object, 'email'), 'description':getattr(restaurant_object, 'description'), 'rating_average':getattr(restaurant_object, 'rating_average')}
    #return HttpResponse(print(context))
    return render(request, 'app/getRestaurantByID.html', context)
