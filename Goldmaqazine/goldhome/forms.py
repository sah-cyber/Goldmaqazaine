from django import forms
from .models import Contact
import re
from django.core.exceptions import ValidationError






class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name','email','message',]
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Adiniz'}),
            'email': forms.TextInput(attrs={'placeholder': 'Email '}),
            #'phone': forms.TextInput(attrs={'placeholder': 'Tel'}),
            'message': forms.Textarea(attrs={'placeholder': 'Mesajiniz', 'class': 'form-control', 'cols': 62, 'rows': 5 })
        }


        def clean_email(self):
            email = self.cleaned_data['email']
            if re.match('admin@mail.ru',email):
                raise ValidationError('Bele email yoxdur')



