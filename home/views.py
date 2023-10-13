from django.shortcuts import render,HttpResponse,render

# Create your views here.



def index(request):

    return render(request ,'index.html')



def about(request):
    return HttpResponse("about")


def booking(request):
    return HttpResponse("booking")


def doctor(request):
    return HttpResponse("doctor")


def contact(request):
    return HttpResponse("contact")


def department(request):
    return HttpResponse("department")
