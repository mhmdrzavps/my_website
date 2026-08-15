
# Create your views here.
from website.models import Contact
from django.shortcuts import render


def home_view(request):
    return render(request, 'website/index.html')

def about_view(request):
    return render(request, 'website/about.html')

def contact_view(request):
    return render(request, 'website/contact.html')

def test(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        subject = request.POST.get('subject')
        email = request.POST.get('email')
        message = request.POST.get('message')
        c = Contact()
        c.name = name
        c.subject = subject
        c.email = email
        c.message = message
        c.save()

        print(name, subject, email, message)



   
    return render(request, 'test.html')