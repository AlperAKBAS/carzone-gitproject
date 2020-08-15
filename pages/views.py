from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
    return render(request, 'pages/home.html',  dict(main_title = 'Our Car Inventory', sub_title = 'Cars'))

def about(request):
    return render(request, 'pages/about.html',  dict(main_title = 'ABOUT US', sub_title = 'ABOUT US'))

def services(request):
    return render(request, 'pages/services.html',  dict(main_title = 'Services', sub_title = 'Services'))

def contact(request):
    return render(request, 'pages/contact.html',  dict(main_title = 'Contact Us', sub_title = 'Contact Us'))

def cars(request):
    """will be updated with modals
    """
    return render(request, 'pages/cars.html', dict(main_title = 'Our Car Inventory', sub_title = 'Cars'))