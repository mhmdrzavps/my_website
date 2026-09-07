from website.models import Contact
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from website.form import NameForm, ContactForm, NewsletterForm
from django.contrib import messages

# Create your views here.
def home_view(request):

    return render(request, 'website/index.html')

def about_view(request):

    return render(request, 'website/about.html')

def contact_view(request):

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'your ticket was submitted')
        else:
            messages.add_message(request, messages.ERROR, 'your ticket was not submitted')
    form = ContactForm()
    return render(request, 'website/contact.html', {'form': form})

def newsletter_view(request):
    if request.method == 'POST':
        form = NewsletterForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        return HttpResponseRedirect('/')

