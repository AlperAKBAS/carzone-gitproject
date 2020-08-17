from django.shortcuts import render

# Create your views here.
def cars(request):
    """will be updated with modals
    """
    return render(request, 'car/cars.html', dict(main_title = 'Our Car Inventory', sub_title = 'Cars'))

