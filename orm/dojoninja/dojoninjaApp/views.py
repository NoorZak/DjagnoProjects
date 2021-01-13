from django.shortcuts import render,redirect
from .models import Dojo,Ninja
# Create your views here.

def root(request):
    context = {

        "dojos" : Dojo.objects.all(),
        }

    return render(request,"index.html",context)

def insertDojo(request):
    if request.POST:
        name= request.POST["name"]
        city = request.POST["city"]
        state = request.POST["state"]

        Dojo.objects.create(name =name ,city =city,state=state)
        return redirect(root)



def insertNinja(request):
    if request.POST:
        fname= request.POST["fname"]
        lname= request.POST["lname"]
        dojoId = request.POST["dojo"]


        Ninja.objects.create(first_name =fname ,last_name=lname,dojo=Dojo.objects.get(id=dojoId))
        return redirect(root)


