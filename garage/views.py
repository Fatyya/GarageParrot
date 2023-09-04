from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import get_user_model
from django.shortcuts import render, redirect
from django.contrib import messages  # Import messages framework

User = get_user_model()

# Create your views here.
from site_client.models import Car, Service, SiteInfo, Testimonial
from garage.forms import SiteInfoForm, ServiceForm, CarForm, TestimonialForm


@login_required
def home(request):
    service = Service.objects.all()
    car = Car.objects.all()
    

    params = {
        'service':service,
        'cars':car
    }
   
    return render(request,'garage/index.html', params)

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect(home)  # Replace 'home' with the actual name of your home view
        else:
            # Handle invalid login
            error_message = "Invalid login credentials."
            return render(request, 'garage/login.html', {'error_message': error_message})
    return render(request, 'garage/login.html')

def logout_view(request):
    logout(request)
    return redirect(login_view)  # Redirect to the login page or any other desired page

def carslist(request):
    car = Car.objects.all()
    
    
    params = {
        'cars':car
    }
    return render(request,'garage/pages/liste_voitures.html',params)



def ajouter_voiture(request):
    
    if request.method == 'POST':
        form = CarForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect(carslist)  # Redirect to car list view after saving

    else:
        form = CarForm()

    params = {
        'form': form,
        
    }
    return render(request,'garage/pages/add_car.html',params)



def service(request):
    services = Service.objects.all()

    if request.method == 'POST':
        form = ServiceForm(request.POST)
        if form.is_valid():
            form.save()
            # After saving, you might want to redirect to avoid re-submission
            return redirect(service)  # Assuming 'service' is the name of the URL

    else:
        form = ServiceForm()

    params = {
        'services': services,
        'form': form
    }
    return render(request, 'garage/pages/service.html', params)



def site_info_view(request):
    site_info = SiteInfo.objects.get_singleton()
    form = SiteInfoForm(instance=site_info)

    if request.method == 'POST':
        form = SiteInfoForm(request.POST, request.FILES, instance=site_info)
        if form.is_valid():
            form.save()

    context = {'form': form}
    return render(request, 'garage/pages/setting.html', context)

from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from garage.forms import CustomUserCreationForm

def ajouter_employer(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        user = form.save()  # Save the form data and retrieve the user instance
        user.is_staff = True 
        user.save() 
        return redirect(staff_list)  # Redirect to the login page
    else:
        form = CustomUserCreationForm()
    context={
        'form':form
    }
    return render(request, 'garage/pages/add-staff.html', context)


def staff_list(request):
    staff_users = User.objects.filter(is_staff=True)
    params = {
        'staff_users':staff_users
    }
    return render(request,'garage/pages/liste-membre.html',params)



def ajout_testimonial(request):
    if request.method == 'POST':
        form = TestimonialForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # Testimonial added successfully
            return redirect(testimonial_list)  # Redirect to the list of testimonials
    else:
        form = TestimonialForm()
    context = {
        'form': form
    }
    return render(request, 'garage/pages/add_testimonial.html', context)

def testimonial_list(request):
    test = Testimonial.objects.all()

    params ={
        'tests':test
    }
    return render(request,'garage/pages/list-testimonial.html',params)