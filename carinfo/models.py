from django.db import models
from django.utils import timezone
from django.urls import reverse



class CarManager(models.Manager):
    def get_queryset(self):
        return super(CarManager,self).get_queryset().filter(in_stock=True)


class Carbrand(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=300,unique=True)
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('carinfo:brand', args=[self.slug])




class  SubCarBrand(models.Model):
    title = models.CharField(max_length=50)
    carbrand = models.ForeignKey(Carbrand,on_delete=models.CASCADE)
    slug = models.SlugField(max_length=50,unique=True)
    
    
    def __str__(self):
        return self.title


class CarInfo(models.Model):
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to='images/',default='images/default.png')
    carbrand = models.ForeignKey(Carbrand,related_name='carbrand',on_delete=models.CASCADE)
    subcarbrand = models.ForeignKey(SubCarBrand,related_name='subcarbrand',on_delete=models.CASCADE)
    created_date = models.DateTimeField(default=timezone.now)
    price_car = models.IntegerField(default=0)
    slug = models.SlugField(max_length=50,unique=True)
    ban_type = models.CharField(max_length=50)
    engine = models.CharField(max_length=50)
    gearbox = models.CharField(max_length=50)
    transmitter = models.CharField(max_length=50)
    describe = models.CharField(max_length=50)
    created_by = models.CharField(max_length=50)
    count_seats = models.IntegerField()
    in_stock = models.BooleanField(default=True)
    objects = models.Manager()
    cars = CarManager()
    
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('carinfo:detail_cars', args=[self.slug])
    
    
