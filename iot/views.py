from django.shortcuts import render
from django.http import JsonResponse
from .forms import *
from main.v2 import *


def home(request):
    return JsonResponse("{'iot'}", safe=False)


def acview(request):
    ls = Ac.objects.get(id=1) 
    if request.method == "POST":
        form = AcIot(request.POST)
        if form.is_valid():
            ac_io = form.cleaned_data["ac_io"]
            ac_temp = form.cleaned_data['ac_temp']
            ls.ac_temp = float(ac_temp)
            ls.ac_io = ac_io
            ls.save()
    else:
        form = AcIot()
    return render(request, 'iot/acio.html', {
        'form' : form
    })



def Tempc(request):
    if request.method == "POST":
        form = AcForm(request.POST)
        print(request.method)
        if form.is_valid():
            ac_io = form.cleaned_data['ac_io']
            ac_temp = form.cleaned_data['ac_temp']
            ac_city = form.cleaned_data['ac_city']
            x = Ac(ac_io=ac_io, ac_temp=ac_temp, ac_city=ac_city)
            x.save()
            ac_temp = float(ac_temp)
            print(f'''
            bool = {ac_io}
            temp = {ac_temp}
            city = {ac_city}
            Data collected
            ''')
    else:
        form = AcForm()
    return render(request, "iot/temp.html", {
        "form" : form
    })


def ac_task(request):
    ls = Ac.objects.get(id=1)
    ls.ac_temp = float(ls.ac_temp)
    task = Tempc2(ls.ac_city, ls.ac_io, ls.ac_temp)
    ap = {
                'ac_temp': ls.ac_temp,
                'city' : ls.ac_city,
                'ac_state' : ls.ac_io,
                'task': task,
            }
    ap = json.dumps(ap)
    ap = json.loads(ap)
    return JsonResponse(ap, safe=False)

