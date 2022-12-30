from django.shortcuts import render


# Create your views here.
def jspiders(request):
    return render(request,'jspiders.html')
def qspiders(request):
    return render(request,'qspiders.html')
