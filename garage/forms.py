from django import forms
from site_client.models import SiteInfo, Car, Service, Testimonial
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User



class SiteInfoForm(forms.ModelForm):
    class Meta:
        model = SiteInfo
        fields = '__all__'
        widgets = {
           
        }
class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = '__all__'
        labels = {
            'prix': 'Prix',
            'image': 'Image',
            'name': 'Model du voiture',
            'description': ' Description ',
            'annee': 'Annee',
            'kilometres': ' Kilometres ',
            # Add other fields and labels as needed
        }
        widgets = {
            # Define your widgets here
        }

class ServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = '__all__'

class CustomUserCreationForm(UserCreationForm):
    first_name = forms.CharField(
        max_length=30,
        required=True,
        help_text='Required.',
        label='Nom :'
    )
    last_name = forms.CharField(
        max_length=30,
        required=True,
        help_text='Required.',
        label='Prenom:'
    )

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')
        labels = {
            'username': 'Nom utilisateur:',
            'email': 'Email:',
            'password1': 'Mot de passe:',
            'password2': 'Confirmer du mot de passe:',
        }


class TestimonialForm(forms.ModelForm):
    class Meta:
        model = Testimonial
        fields = ('nom_client', 'temoinages_content', 'avatar_image')  # Include the fields you want in the form
