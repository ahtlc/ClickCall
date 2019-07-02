from django import forms
from django.forms import DateTimeField
from calls.models import Contact, Tag, Call


class ContactForm(forms.ModelForm):
    """
    Form that handles the contact creation
    """
    raw_tags = forms.CharField(widget=forms.HiddenInput())

    def save(self, commit=True):
        tags_name = self.cleaned_data.get('raw_tags').split(',') 
        # TODO: create the m2m relationship
        for tag_name in tags_name:
            if Tag.objects.filter(name=tag_name).exists():
                pass
            # create the relationship if the tag exists
            else:
                Tag.objects.create(
                    name=tag_name)
            # create the relationship if the tag doesn't exists

        return super().save()

    class Meta:
        model = Contact
        fields = '__all__'
        exclude = ['tag', 'last_update', 'status']

class CallSchedulingForm(forms.ModelForm):
    # date_scheduling = DateTimeField(input_formats=["%d %m %Y %H:%M"])
    class Meta:
        model = Call
        fields = ['date_scheduling']

class ChangePriceForm(forms.ModelForm):
    class Meta:
        model = Call
        fields = ['value']
       
class NotesForm(forms.ModelForm):
    class Meta:
        model = Call
        fields = ['notes']
        # fields = '__all__'
