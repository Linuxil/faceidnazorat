from django import forms
from .models import Users

class YourModelForm(forms.ModelForm):
    class Meta:
        model = Users
        fields = ['image','phone','first_name','last_name','username','password']