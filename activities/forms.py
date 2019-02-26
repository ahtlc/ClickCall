from django import forms
from calls.models import Contact

class contactForm(forms.ModelForm):

  class Meta:
    model = Contact
    fields = '__all__'

  