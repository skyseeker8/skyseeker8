from django.http import HttpResponse
import re
from django.utils.timezone import datetime
from django.http import HttpResponse
from django.shortcuts import render


    
    

def about(request):
    now = datetime.now()
    formatted_now = now.strftime("%A, %d %B, %Y at %X")
    return render(request, "hello/about.html",{
        'date': datetime.now(),
        'aclass' : "navbar-brand",
        'hclass' : "navbar-item",
        'cclass' : "navbar-item"
    })

def contact(request):
    now = datetime.now()
    formatted_now = now.strftime("%A, %d %B, %Y at %X")
    return render(request, "hello/contact.html",{
        'date': datetime.now(),
        'cclass' : "navbar-brand",
        'hclass' : "navbar-item",
        'aclass' : "navbar-item"
    })

def hello_there(request, name):
    now = datetime.now()
    formatted_now = now.strftime("%A, %d %B, %Y at %X")

    # Filter the name argument to letters only using regular expressions. URL arguments
    # can contain arbitrary text, so we restrict to safe characters only.
    match_object = re.match("[a-zA-Z]+", name)

    if match_object:
        clean_name = match_object.group(0)
    else:
        clean_name = "Friend"

    content = "Hello there, " + clean_name + "! It's " + formatted_now
    return HttpResponse(content)

def hello_there(request, name):
    return render(
        request,
        'hello/hello_there.html',
        {
            'name': name,
            'date': datetime.now()
        }
    )
def home(request):
    return render(
        request,
        "hello/home.html",{
        'date': datetime.now(),
        'hclass' : "navbar-brand",
        'aclass' : "navbar-item",
        'cclass' : "navbar-item"
    })
    
