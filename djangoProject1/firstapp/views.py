from django.shortcuts import render
from django.http import HttpResponse
from firstapp.models import Contact


# Create your views here.


def index(request):
    context=({'name':'Jiby', 'course':'Django'})
    return render(request, "home.html", context)


def contact(request):
    context = ({'name': 'Jiby', 'course': 'Django'})
    if request.method == 'POST':
        tname= request.POST['tname']
        temail = request.POST["email"]
        phone = request.POST["phone"]
        tconcern = request.POST["concern"]
        ins = Contact(name=tname, email=temail, phone=phone, concern=tconcern)
        ins.save()
        print("that data has been inserted")
    return render(request, 'contact.html', context)





def about(request):
    context = ({'name': 'Jiby', 'course': 'Django'})
    return render(request, 'about.html', context)

