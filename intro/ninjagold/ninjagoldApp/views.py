from django.shortcuts import render, HttpResponse,redirect
from django.http import JsonResponse
import random
# Create your views here.
def root(request):
    if "money" not in request.session:
        request.session["money"]=0
    if "text" not in request.session:
        request.session["text"]=""

    return render(request, "index.html")


def process_money(request):
    action= "earned"
    val =0
    msg=""
    if request.POST:
        type = request.POST["type"]
        if type =="farm":
            val =random.randint(10, 20)
            request.session["money"]+=val

        elif type == "cave":
            val =random.randint(5, 10)
            request.session["money"]+=val

        elif type == "house":
            val =random.randint(2, 5)
            request.session["money"]+=val

        elif type == "casino":

            val =random.randint(0, 50)
            ch = random.randint(0,2)
            if ch ==0:
                action = "earned"
                request.session["money"] += val

            if ch == 1:
                action="lost"
                request.session["money"]-=val


            request.session["money"]= val

        if action=="earned":
            msg =action+str(val)+"golds from the"+type+"\n"
        elif action=="lost":
            msg ="Entered a"+type+"and"+action+str(val)+"golds .. Ouch\n"

        request.session["text"]+=msg
        request.session["action"]=action

        return render(request, "index.html")

def restart(request):
        if "money" in request.session:
            del request.session["money"]
        if "text"  in request.session:
            del request.session["text"]

        return redirect(root)

    #del request.session['num']
    #return redirect(root)
