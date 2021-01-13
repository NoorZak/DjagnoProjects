from django.shortcuts import render, HttpResponse,redirect
from django.http import JsonResponse

# Create your views here.



def root(request):

    if 'counter' in request.session:
        request.session['counter'] += 1
    else:
        request.session['counter'] = 0

    return render(request, 'index.html')



def destroy(request):

    if 'counter' in request.session:
         del request.session['counter']
    return redirect(root)
