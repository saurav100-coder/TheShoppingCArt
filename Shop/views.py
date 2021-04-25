from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
import datetime

# Create your views here.
def home(request):
    return render(request, 'index.html')


def about(request):
    return HttpResponse( "<h1>this is about page</h1>")


def contact(request):
    return HttpResponse( "<h1>this is contact page</h1>")

def services(request):
    return HttpResponse( "<h1>this is service page</h1>")

def page_not_found(request):
    now = datetime.datetime.now()
    html = "<h1>%s</h1> <h1> Error in loading</h1><h1>Error 404... Page Not Found !</h1>" %now
    return HttpResponse(html)
