from django.shortcuts import render
from .forms import contactForm
from django.views import generic

def contact_new(request):
    if request.method == "POST":
         form = contactForm(request.POST)
         if form.is_valid():
             contact = form.save(commit=False)
             contact.save()
    else:
        form = contactForm()
    return render(request, '.html', {'form': form})

class CallModalView(generic.TemplateView):
    template_name='call-modal.html'
    def get_context_data(self, **kwargs):
        context = super(CallModalView, self).get_context_data(**kwargs)
        context['range'] = range(4)
        return context