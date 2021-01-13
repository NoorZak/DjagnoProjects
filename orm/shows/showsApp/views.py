from django.shortcuts import render,redirect
from .models import show
from django.contrib import messages
from django.urls import reverse


# Create your views here.

def root(request):
    context = {

        "shows" : show.objects.all(),
        }

    return render(request,"index.html",context)
#
# def insert(request):
#     if request.POST:
#         first_name1= request.POST["first_name"]
#         last_name1 = request.POST["last_name"]
#         age1 = request.POST["age"]
#         email1 = request.POST["email"]
#
#         user.objects.create(first_name =first_name1 ,last_name =last_name1,email_address=email1,age=age1)
#         return redirect(root)
#
#
def viewShow(request,my_val):

    context = {

        "show": show.objects.get(id=my_val),
       }

    return render(request,"viewShow.html",context)

def deleteShow(request,my_val):
    show_to_delete = show.objects.get(id=my_val)  # let's retrieve a single movie,
    show_to_delete.delete()

    return redirect(root)

def goToInsert(request):
    return render(request,"insertShow.html")

def insertShow(request):

    if request.POST:
        errors = show.objects.basic_validator(request.POST)
        # check if the errors dictionary has anything in it
        if len(errors) > 0:
            # if the errors dictionary contains anything, loop through each key-value pair and make a flash message
            for key, value in errors.items():
                messages.error(request, value)

            return render(request, "insertShow.html")
        else:
            show.objects.create(title=request.POST["title"],desc=request.POST["desc"],release_date=request.POST["release_date"],network=request.POST["network"])

            return redirect(reverse(viewShow, kwargs={"my_val": show.objects.last().id}))



def goToEdit(request,my_val):
    context={
        my_val:my_val
    }
    return render(request,"editShow.html",context)

def editShow(request,my_val):

    show_to_update = show.objects.get(id=my_val)  # let's retrieve a single movie,
    if request.POST:
        errors = show.objects.basic_validator(request.POST)
        # check if the errors dictionary has anything in it
        if len(errors) > 0:
            # if the errors dictionary contains anything, loop through each key-value pair and make a flash message
            for key, value in errors.items():
                messages.error(request, value)

            return redirect(reverse(goToEdit, kwargs={"my_val": my_val}))
        else:
            show_to_update.title = request.POST["title"]
            show_to_update.network = request.POST["network"]

            show_to_update.desc = request.POST["desc"]
            show_to_update.release_date = request.POST["release_date"]
            show_to_update.save()

            return redirect(reverse(viewShow, kwargs={"my_val": my_val}))


