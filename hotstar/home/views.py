from django.shortcuts import render, HttpResponse
from home.models import Register

# Create your views here.
def register(request):
    if request.method == 'POST':
        name = request.POST.get("name")
        username = request.POST.get("username")
        mobile = request.POST.get("mobile")
        email = request.POST.get("email")
        password = request.POST.get("password")

        new_register = Register(
            name=name,
            username=username,
            mobile=mobile,
            email=email,
            password=password
        )
        new_register.save()
        return HttpResponse("User Registerd Successfully")

    return render(request, 'register.html')

def login(request):
    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = Register.objects.filter(username=username, password=password).first()
        if user:
            return HttpResponse(f"Welcome Back, {username}")
        else:
            return HttpResponse("Record not Found, Register First!")

    return render(request, 'login.html')
