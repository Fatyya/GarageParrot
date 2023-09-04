from django import forms

class CarFilterForm(forms.Form):
    price_range = forms.IntegerField(
        label="Price Range",
        widget=forms.NumberInput(attrs={'type': 'range', 'min': 1000, 'max': 50000, 'step': 1000})
    )
    km_range = forms.IntegerField(
        label="Kilometers Range",
        widget=forms.NumberInput(attrs={'type': 'range', 'min': 0, 'max': 100000, 'step': 1000})
    )
    year_range = forms.IntegerField(
        label="Year Range",
        widget=forms.NumberInput(attrs={'type': 'range', 'min': 1990, 'max': 2023, 'step': 1})
    )
