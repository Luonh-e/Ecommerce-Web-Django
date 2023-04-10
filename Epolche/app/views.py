from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    context= {}
    return render(request, 'app/home.html')
def cart(request):
    context= {}
    return render(request, 'app/cart.html')
def payment(request):
    context= {}
    return render(request, 'app/payment.html')
