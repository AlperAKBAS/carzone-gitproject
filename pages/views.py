from django.shortcuts import render, HttpResponse
from .models import Team
from car.models import Car
from django.db.models import Avg, Max, Min
# Create your views here.
def home(request):
    team = Team.objects.all()
    featured_cars = Car.objects.all().order_by('-created_date').filter(is_featured=True)
    latest_cars = Car.objects.all().order_by('-created_date')
    # search_fields = Car.objects.values('model', 'city', 'year', 'body_style').distinct()
    model_search = sorted(Car.objects.values_list('model', flat=True).distinct())
    city_search = sorted(Car.objects.values_list('city', flat=True).distinct())
    year_search = sorted(Car.objects.values_list('year', flat=True).distinct())
    body_style_search = sorted(Car.objects.values_list('body_style', flat=True).distinct())
    prices = sorted(Car.objects.values_list('price', flat=True).distinct())
    min_price = Car.objects.all().aggregate(Min('price')).get('price__min')
    max_price = Car.objects.all().aggregate(Max('price')).get('price__max')
    data = dict(
        model_search=model_search,
        city_search=city_search,
        year_search=year_search,
        body_style_search=body_style_search,
        min_price=min_price,
        max_price=max_price,
        team = team,
        featured_cars = featured_cars,
        latest_cars = latest_cars,
        main_title = 'Our Car Inventory', 
        sub_title = 'Cars'
        )
    return render(request, 'pages/home.html', context=data)



def about(request):
    team = Team.objects.all()
    context = dict(
        team = team,
        main_title = 'ABOUT US', 
        sub_title = 'ABOUT US'
        )
    return render(request, 'pages/about.html', context=context)


 
def services(request):
    return render(request, 'pages/services.html',  dict(main_title = 'Services', sub_title = 'Services'))

def contact(request):
    return render(request, 'pages/contact.html',  dict(main_title = 'Contact Us', sub_title = 'Contact Us'))

