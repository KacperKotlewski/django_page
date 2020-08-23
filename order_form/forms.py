from django import forms
from .models import Orders
from django.utils.translation import ugettext_lazy as _

class Order(forms.ModelForm):
    class Meta:
        model = Orders
        fields = ['product', 'name', 'surname', 'email', 'phone', 'adress', 'house_number', 'city_name', 'zip_code', 'count']
        labels = {
            'name': _('Imię'),
            'surname': _('Nazwisko'),
            'email': _('E-mail'),
            'phone': _('Telefon'),
            'count': _('ilosc'),
            'adress': _('ulica'),
            'house_number': _('numer domu/lokalu'),
            'zip_code': _('kod pocztowy'),
            'city_name': _('miasto'),
        }
    
    def __init__(self, *args, **kwargs):
        super(Order, self).__init__(*args, **kwargs)
        # ... existing code...
        self.fields['count'].widget.attrs['min'] = 1
        self.fields['count'].widget.attrs['max'] = 10
        self.fields['count'].initial = 1
        self.fields['product'].widget = forms.HiddenInput()