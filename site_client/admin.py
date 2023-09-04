from django.contrib import admin
from .models import Service , Testimonial, Slider, SiteInfo, Car
# Register your models here.
@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    '''Admin View for Service'''

    list_display = ('nom_service','description')

@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    '''Admin View for Testimonial'''

    list_display = ('nom_client','temoinages_content')
@admin.register(Slider)
class SliderAdmin(admin.ModelAdmin):
    '''Admin View for Slider'''

    list_display = ('image','caption',)
    
@admin.register(SiteInfo)
class SiteInfoAdmin(admin.ModelAdmin):
    '''Admin View for SiteInfo'''

    list_display = ('nom_site','address')
  

@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    '''Admin View for Car'''

    list_display = ('prix','image','name','description','annee','kilometres')
    list_filter = ('prix','annee','kilometres')
   