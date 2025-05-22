from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'input-field', 'placeholder': "Ismingiz"}),
            'email': forms.EmailInput(attrs={'class': 'input-field', 'placeholder': "Email manzilingiz"}),
        }