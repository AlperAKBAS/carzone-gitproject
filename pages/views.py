from django.shortcuts import render, HttpResponse
from .models import Team

# Create your views here.
def home(request):
    team = Team.objects.all()
    context = dict(
        team = team,
        main_title = 'Our Car Inventory', 
        sub_title = 'Cars'
        )
    return render(request, 'pages/home.html', context=context)



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

def cars(request):
    """will be updated with modals
    """
    return render(request, 'pages/cars.html', dict(main_title = 'Our Car Inventory', sub_title = 'Cars'))