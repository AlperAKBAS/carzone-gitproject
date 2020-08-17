from django.shortcuts import render, HttpResponse
from .models import Team
from car.models import Car

# Create your views here.
def home(request):
    team = Team.objects.all()
    featured_cars = Car.objects.all().order_by('-created_date').filter(is_featured=True)
    latest_cars = Car.objects.all().order_by('-created_date')
    data = dict(
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

