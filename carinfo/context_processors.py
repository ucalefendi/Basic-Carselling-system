from django.shortcuts import render,get_object_or_404
from .models import CarInfo,Carbrand,SubCarBrand


def carbrands(request):
    return {
        'carbrands': Carbrand.objects.all()
    }



