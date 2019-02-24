from django import forms
from calls.models import Contact

class contactForm(forms.ModelForm):

  class Meta:
    model = Contact
    fields = '__all__'

  def clean(self):
    cleaned_data = super().clean()
    content = self.cleaned_data.get('content')
    return cleaned_data