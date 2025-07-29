from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
    return HttpResponse("This is my Homepage!😍")

def contact(request):
    return HttpResponse("This is my Contact Page©️")

def about(request):
    return HttpResponse("This is my About Us page💻")

def service(request):
    return HttpResponse("This is my Service Page📞")