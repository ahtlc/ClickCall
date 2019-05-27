from django import forms
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

    class Meta:
        model = Call
        fields = ['date_scheduling']
