from django import forms
from .models import Iphone

class IphoneForm(forms.ModelForm):

    class Meta:
        model = Iphone
        fields = '__all__'