from socket import fromshare
from django import forms
from .models import Email,Contact
from django.forms import TextInput,EmailInput,IntegerField



class EmailForm(forms.ModelForm):
    
    class Meta:
        model=Email
        fields = "__all__"



class ContactForm(forms.ModelForm):
    
    class Meta:
        model=Contact
        fields = "__all__"


        widgets = {
            'name': TextInput(),
            'email': EmailInput(),
            'phone': IntegerField(),
            'message': TextInput()
        }

