from django.shortcuts import render, HttpResponse,redirect
from django.http import JsonResponse
import random
# Create your views here.
def root(request):
    msg=""

    playagain=False
    if 'num' not in request.session:
         request.session["num"]=random.randint(1,100)
    if request.POST:
        newnum=int(request.POST["newnum"])

        msg = guess(newnum,int(request.session["num"]))
        if msg=="You Found The Num":
             playagain=True

    context ={
    "msg": msg,
    "playagain":playagain

         }
    return render(request,"index.html",context)

def again(request):
    del request.session['num']
    return redirect(root)

def guess(newmum,num):
    if newmum>num:
        str="Too High"

    elif newmum < num:
        str = "Too Low"

    elif newmum == num:
        str = "You Found The Num"

    return str
