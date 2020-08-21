from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from .models import Car
from django.db.models import Avg, Max, Min
# Create your views here.


class CarListView(ListView):
    model = Car
    template_name = 'car/cars.html'
    context_object_name = 'Cars'
    ordering = '-created_date'
    paginate_by = 6

    def get_context_data(self,**kwargs):
        context = super(CarListView,self).get_context_data(**kwargs)

        model_search = sorted(Car.objects.values_list('model', flat=True).distinct())
        city_search = sorted(Car.objects.values_list('city', flat=True).distinct())
        year_search = sorted(Car.objects.values_list('year', flat=True).distinct())
        body_style_search = sorted(Car.objects.values_list('body_style', flat=True).distinct())
        prices = sorted(Car.objects.values_list('price', flat=True).distinct())
        min_price = Car.objects.all().aggregate(Min('price')).get('price__min')
        max_price = Car.objects.all().aggregate(Max('price')).get('price__max')

        context['main_title'] = 'Our Car Inventory'
        context['sub_title'] = 'Cars'
        context['city_search'] = city_search
        context['model_search'] = model_search
        context['year_search'] = year_search
        context['body_style_search'] = body_style_search
        context['prices'] = prices
        context['min_price'] = min_price
        context['max_price'] = max_price
        return context


def car_detail(request,id):
    car_obj = get_object_or_404(Car,pk=id)
    data = dict(
        car=car_obj,
        main_title =  car_obj.car_title, 
        sub_title = car_obj.car_title,
    )
    return render(request, 'car/car-details.html', data)



def search(request):

    cars = Car.objects.all()
    ### her defasında cars isimli değişkeni filter ediyoruz, yeni bir databas sorgusu yapmıyoruz!!!!!

    ####CREATE OPTION VALUES
    model_search = sorted(Car.objects.values_list('model', flat=True).distinct())
    city_search = sorted(Car.objects.values_list('city', flat=True).distinct())
    year_search = sorted(Car.objects.values_list('year', flat=True).distinct())
    body_style_search = sorted(Car.objects.values_list('body_style', flat=True).distinct())
    prices = sorted(Car.objects.values_list('price', flat=True).distinct())
    transmission = sorted(Car.objects.values_list('transmission', flat=True).distinct())
    min_price = Car.objects.all().aggregate(Min('price')).get('price__min')
    max_price = Car.objects.all().aggregate(Max('price')).get('price__max')


    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword: #not blank
            cars = cars.filter(description__icontains=keyword)

    else:
        keyword = None

    if 'select-model' in request.GET:
        model = request.GET['select-model']
        if model: #not blank
            cars = cars.filter(model__iexact=model)

    if 'select-location' in request.GET:
        keyword = request.GET['select-location']
        if keyword: #not blank
            cars = cars.filter(city__iexact=keyword)

    if 'select-year' in request.GET:
        year = request.GET['select-year']
        if year: #not blank
            cars = cars.filter(year__iexact=year)

    if 'select-type' in request.GET:
        tip = request.GET['select-type']
        if tip: #not blank
            cars = cars.filter(body_style__iexact=tip)

    if 'min_price' in request.GET:
        min_price = request.GET['min_price']
        max_price = request.GET['max_price']
        if max_price:
            cars = cars.filter(price__gte=min_price, price__lte=max_price)

    if 'transmission' in request.GET:
        transmission = request.GET['transmission']

        if transmission:
            cars = cars.filter(transmission__iexact=transmission)

    data = dict(
        cars = cars,
        model_search=model_search,
        city_search=city_search,
        transmission=transmission,
        year_search=year_search,
        body_style_search=body_style_search,
        min_price=min_price,
        max_price=max_price,
        main_title =  'Search Page', 
        sub_title = f'Results for {keyword}' if keyword else 'Make a Search',  
    )
    return render(request, 'car/search.html', context= data)