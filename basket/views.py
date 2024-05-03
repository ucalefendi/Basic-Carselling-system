from django.shortcuts import render,get_object_or_404
from carinfo.models import Carbrand,CarInfo,SubCarBrand
from django.http import JsonResponse
from .basket import Basket




def basket_summary(request):
    return render(request,'basket.html')




def basket_add(request):
    basket = Basket(request)
    if request.POST.get('action') == 'post':
        car_id = int(request.POST.get('car_id'))
        car = get_object_or_404(CarInfo,id=car_id)
        basket.add(car=car)
        response = JsonResponse({'test':'data'})
        return response
        
    # return render(request,'detail_cars.html')