# This is manually Created
from django.http import HttpResponse
from django.shortcuts import render # For using templates

def home(request):
    params = {'Created' : 'Suman Khatua', 
              'Place': 'Haldia'}
    return render(request, 'home.html', params)

def contact(request):
    params = {'Created' : 'Suman Khatua', 
            'Place': 'Haldia'}
    user_name = request.POST.get('user_name', None)
    print(user_name)
    return render(request, 'contact_us.html', params)