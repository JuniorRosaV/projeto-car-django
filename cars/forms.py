from django import forms
from cars.models import Car

class CarModelForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = '__all__'
        
    def clean_value(self):
        value = self.cleaned_data.get('value')
        if value < 10000:
            self.add_error('value','Não aceitamos valores abaixo de R$ 10.000')
        return value
    
    def clean_data(self):
        data = self.cleaned_data.get('factory_year')
        if data < 2000:
            self.add_error('data','Não aceitamos carros inferiores aos anos 2000')
        return data
    