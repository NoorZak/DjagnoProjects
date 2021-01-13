from django.shortcuts import render

# Create your views here.

def root(request):
    return render(request,"index.html")

def result(request):
    context = {
        "name": request.POST["name"],
        "comment": request.POST["comment"],
        "language":request.POST["language"],
        "location":request.POST["location"]
    }
    return render(request, "result.html", context)
