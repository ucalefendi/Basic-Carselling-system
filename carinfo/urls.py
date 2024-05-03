
from django.urls import path
from . import views 
# from .context_processors import brand

app_name = 'carinfo'

urlpatterns = [
    path('',views.home_page,name='home'),
    path('item/<slug:slug>/',views.detail_cars,name='detail_cars'),
    path('featured-cars/',views.featured_cars,name='featured_cars'),
    path('brand/<slug:brand_slug>/',views.brand,name='brand'),
    path('new-cars/',views.new_cars,name='new_cars'),
    path('all-cars/',views.all_cars,name='all_cars'),
   
]
