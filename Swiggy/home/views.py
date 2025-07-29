from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home/home.html')

def contact(request):
    context = {
        'name': "Vishal Kumar"
    }
    return render(
                   request, 
                   'contact.html', 
                    context=context
                  )

def about(request):
    return render(request, 'about.html')

def gallary(request):
    return render(request, 'gallary.html')