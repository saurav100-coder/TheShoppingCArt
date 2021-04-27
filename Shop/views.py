from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
import datetime

from .models import Seller, Customer
from .forms import CustomerForm, SellerForm
# Create your views here.


def home(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about/about.html')


def contact(request):
    return render(request, 'about/contact.html')


def careers(request):
    return render(request, 'about/careers.html')


def page_not_found(request):
    now = datetime.datetime.now()
    html = "<h1>%s</h1> <h1> Error in loading</h1><h1>Error 404... Page Not Found !</h1>" % now
    return HttpResponse(html)


def get_customer(request):
    form = CustomerForm()
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            phone = form.cleaned_data['phone']
            address = form.cleaned_data['address']
            password = form.cleaned_data['password']
            customer = Customer(name=name, email=email, phone=phone, address=address, password=password)
            customer.save()
            return redirect('home')

    return render(request, 'signup_customer.html', {'form': form})



def test_page(request):
    return render(request, 'about/careers.html')
