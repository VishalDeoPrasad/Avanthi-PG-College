from django.shortcuts import render, redirect, HttpResponse
from .models import Register, Product
from django.contrib import messages

# Home Page – Show all products
def home(request):
    products = Product.objects.all()
    return render(request, 'home.html', {'products': products})

# Register View
def register_view(request):
    if request.method == 'POST':
        name = request.POST.get("name")
        username = request.POST.get("username")
        mobile = request.POST.get("mobile")
        email = request.POST.get("email")
        password = request.POST.get("password")

        Register.objects.create(
            name=name,
            username=username,
            mobile=mobile,
            email=email,
            password=password
        )
        return HttpResponse("Registration Successful! <a href='/login/'>Login Here</a>")
    return render(request, 'register.html')

# Login View
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = Register.objects.filter(username=username, password=password).first()
        if user:
            request.session['username'] = username
            return HttpResponse(f"Welcome {username}! <a href='/'>Go Home</a>")
        else:
            return HttpResponse("Invalid Credentials! <a href='/register/'>Register Here</a>")
    return render(request, 'login.html')

# Cart Page
def cart(request):
    cart_items = request.session.get('cart', [])
    products = Product.objects.filter(id__in=cart_items)
    return render(request, 'cart.html', {'products': products})

# Add to Cart Function
def add_to_cart(request, id):
    cart = request.session.get('cart', [])
    if id not in cart:
        cart.append(id)
        messages.success(request, "Product added to cart!")
    else:
        messages.info(request, "Product is already in the cart.")
    request.session['cart'] = cart
    return redirect('/')


# Checkout Page
def checkout(request):
    # Clear the cart after checkout
    request.session['cart'] = []
    return render(request, 'checkout.html')

def logout_view(request):
    """
    Clears session (logout user).
    """
    request.session.flush()
    return HttpResponse("You have been logged out. <a href='/'>Go Home</a>")

