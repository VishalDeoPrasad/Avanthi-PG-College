from django.shortcuts import render, HttpResponse
# Dictionary to store user credentials (username: password)
users = {
    "admin": "1234",
    "user1": "password",
    "vishal": "securepass"
}
def login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        if username in users and users[username] == password:
            return HttpResponse(f"<h2>Welcome, {username}! Login successful. ✅</h2>")
        else:
            return HttpResponse("<h2 style='color: red;'>Invalid username or password! ❌</h2>")
   
    return render(request, "login.html")

from .models import Contact

def contact(request):
    message = ""
    if request.method == "POST":
        name = request.POST.get("name")
        mobile = request.POST.get("mobile")
        email = request.POST.get("email")
        description = request.POST.get("description")

        # Save the data into the database
        Contact.objects.create(name=name, mobile=mobile, email=email, description=description)
       
        message = "Your message has been submitted successfully! ✅"

    return render(request, "contact.html", {"message": message})