from django.shortcuts import render
from .models import Contact
from .forms import contactForm

  def contact_new(request):
    if request.method == "POST":
      form = contactForm(request.POST)
      if form.is_valid():
        contact = form.save(commit=False)
        contact.save()
    else: 
      form = contactForm()
    return render (request, '.html',{'form': form})

