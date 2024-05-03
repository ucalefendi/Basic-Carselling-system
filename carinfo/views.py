from django.shortcuts import render,get_object_or_404
from .models import CarInfo,Carbrand,SubCarBrand


def home_page(request):
    return render(request,'base.html')

def all_cars(request):
    all_cars = CarInfo.cars.all()
    context = {'all_cars':all_cars}
    return render(request,'all_cars.html',context)
    

def featured_cars(request):
    featured_cars_query = CarInfo.objects.all().filter(created_date__lte='2024-04-04')
    context = {'featured_cars':featured_cars_query}
    return render(request,'featured_cars.html',context)


def detail_cars(request,slug):
    car_details = get_object_or_404(CarInfo,slug=slug,in_stock=True)
    context = {'car_detail':car_details}
    return render(request,'detail_cars.html',context)

def brand(request,brand_slug):
    brand = get_object_or_404(Carbrand,slug=brand_slug)
    cars = CarInfo.objects.filter(carbrand=brand)
    context = {'brand':brand,
               'cars':cars
               }
    
    return render(request,'brand.html',context)

    


def new_cars(request):
    return render(request,'new_cars.html')
