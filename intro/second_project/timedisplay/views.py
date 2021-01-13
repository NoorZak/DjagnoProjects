from django.shortcuts import render

from time import strftime, localtime

def time(request):
    time={
        'time': strftime('%I:%M %p',localtime()),
        'date': strftime('%A %B %d'),
    }

    return render(request,'index.html', time)