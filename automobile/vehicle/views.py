from django.shortcuts import render,redirect
from vehicle.models import Car
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

# Create your views here.
def find(request):
    result = Car.objects.all()
    if request.method=="POST":
        na = str(request.POST.get('na'))
        if Car.objects.filter(id=na).exists():
            b = Car.objects.get(id=na)
        else:
            b = None
        return render(request,'home.html',{'res':result,'re':b})
    return render(request,'home.html',{'res':result})   

def addinfo(request):
    result=Car.objects.all()
    if request.method=="POST":
        a=request.POST.get('a')
        b=request.POST.get('b')
        c=request.POST.get('c')
        if a and b and c:
            obj=Car(name=a,color=b,fuel=c)
            obj.save()
        return redirect('addinfo')
    result = Car.objects.all()
    return render(request,'insert.html',{'re':result})

def user(request):
    result=User.objects.all
    return render(request,'user.html',{'res':result})


def users(request):
    b = None
    if request.method == "POST":
        n = request.POST.get('n')
        b = User.objects.filter(username=n).exists()
        return render(request, 'find.html', {'b': b})
    return render(request, 'find.html', {'b': b})

def Ausers(request):
    b = None
    if request.method == "POST":
        n = request.POST.get('n')
        p = request.POST.get('p')
        user = authenticate(request, username=n, password=p)
        b = user is not None
        return render(request, 'Auth.html', {'b': b})
    return render(request, 'Auth.html', {'b': b})