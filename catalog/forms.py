from django import forms
from catalog.models import Product, Versions
a = 'казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар'



class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

    def clean_name(self):
        cleaned_data = self.cleaned_data.get('name')
        for i in a:
            if i in cleaned_data:
                raise forms.ValidationError('нормально пиши')

        return cleaned_data

class VersionsForm(forms.ModelForm):
    class Meta:
        model = Versions
        fields = '__all__'

