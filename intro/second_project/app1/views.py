from django.shortcuts import render, HttpResponse,redirect
from django.http import JsonResponse

# Create your views here.
def root(request):
    return redirect("/blogs")



def index(request):
    return HttpResponse("placeholder to display blog number")


def new(request):
    return HttpResponse("placeholder to display blog number")


def create(request):
    return redirect("/")


def show(request,number):
    return HttpResponse(f"placeholder to display blog number:{number}")

def destroy(request,number):
    return redirect("/blogs")

def edit(request,number):
    return HttpResponse(f"placeholder to display blog number:{number}")

def json(request):
    return JsonResponse({"title": "myfirstblog", "content": "Lorim,Ipsum dolor sit amet"})
