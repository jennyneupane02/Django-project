from django.shortcuts import render


def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


def contact(request):
    name = None
    message = None

    if request.method == "POST":
        name = request.POST.get("name")
        message = request.POST.get("message")

    return render(request, 'contact.html', {
        "name": name,
        "message": message
    })
