from django.shortcuts import render , redirect
from django.http import HttpResponse
from appl.models import *
from userapp.models import Regisdb,Vehicle,VehicleImage 

# Create your views here.

def index(request):
    return render(request,"index-copy.html")

def addcat(request):
    if request.method == 'POST':
        name = request.POST['name']

        category.objects.create(
            catname = name,
        )
    return render(request,"addcat.html")


def viewcat(request):
    viewcategory = category.objects.all()
    context = {
        'viewcategory' : viewcategory,
    }

    return render(request,"viewcat.html",context)
    
    


def filters(request, catid):
    filtercat = category.objects.filter(id=catid)
    context = {
        'filtercat':filtercat,
    }
    return render(request,"updat.html",context)



def delete(request, catid):
    category.objects.filter(id=catid).delete()
    return render(request,"delete")


def updatecat(request, catid):
    if request.method =='POST':
        name = request.POST['name']
        

        category.objects.filter(id=catid).update(
            catname = name,
            
        )
        return redirect('viewcat')
    return render(request, "viewcat.html")



def addbrand(request):
    if request.method == 'POST':
        name = request.POST['name']

        Brands.objects.create(
            brandname = name,
        )
    return render(request,"addbrand.html")


def viewbrand(request):
    viewbrand = Brands.objects.all()
    context = {
        'viewbrand' : viewbrand,
    }

    return render(request,"viewbrand.html",context)



def filter(request, br_id):
    filterbrand = Brands.objects.filter(id=br_id)
    context = {
        'filterbrand':filterbrand,
    }
    return render(request,"updt.html",context)


def deletebr(request, br_id):
    Brands.objects.filter(id=br_id).delete()
    return render(request,"deletebr")







def dup(request):    
    return render(request,"dup.html")


def sample(request):
    return render(request, "sample.html")


def view_user(request):
    users = Regisdb.objects.all()
    context = {"users": users}
    return render(request, 'view_user.html', context)


def view_product(request):
    products = Vehicle.objects.all()
    context = {
        'products': products,
    }
    return render(request, 'view_product.html', context)

def userlogout(request):
    del request.session['name_u']
    del request.session['u_id']
    del request.session['phonenumber_u']
    del request.session['email_u']
    del request.session['username_u']
    del request.session['password_u']
    return redirect('login')