from django.shortcuts import render
from .models import Service, Slider, Testimonial, Car
from .forms import CarFilterForm

# Create your views here.
def page_accueil(request):
    service = Service.objects.all()[:6]
    testimonial = Testimonial.objects.all()
    slider = Slider.objects.all()
    car = Car.objects.all()
   
   
    params ={
        'services':service,
        'testimonials':testimonial,
        'slider':slider,
        'cars':car,
    }


    return render(request,'site_client/index.html', params)