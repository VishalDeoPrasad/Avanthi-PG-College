from django.shortcuts import render, HttpResponse

db = {
    "vishal": "12345",
    "amit" : "00000",
    "rahul" : "11111"
}

def login(request):
    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")

        if username in db:
            if password == db[username]:
                return HttpResponse(f"Welcome to facebook Application, {username}")
            else:
                return HttpResponse("Incorrect Password!✖️")
        else:
            return HttpResponse("Username Didn't Exist⚡")


    return render(request, 'login.html')
