from django.urls import path
from . import views

urlpatterns = [
    path('', views.CarListView.as_view(), name='cars'),
    path('<int:id>', views.car_detail, name='car-detail'),
    path('search/', views.search, name='search'),
]
