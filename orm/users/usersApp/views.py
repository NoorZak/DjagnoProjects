from django.shortcuts import render,redirect
from .models import user
# Create your views here.

def root(request):
    context = {

        "users" : user.objects.all(),
        }

    return render(request,"index.html",context)

def insert(request):
    if request.POST:
        first_name1= request.POST["first_name"]
        last_name1 = request.POST["last_name"]
        age1 = request.POST["age"]
        email1 = request.POST["email"]

        user.objects.create(first_name =first_name1 ,last_name =last_name1,email_address=email1,age=age1)
        return redirect(root)


