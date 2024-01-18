from django.shortcuts import render , redirect ,get_object_or_404
from django.http import HttpResponse ,JsonResponse
from userapp.models import *
from .models import Vehicle, VehicleImage,Brands
from .models import Room, Message
from django.contrib.auth.models import User




# Create your views here.
def index(request):
    return render(request,"index.html")







 

def sell(request):
    var = request.session.get('u_id')
    if var in request.session:
        product = category.objects.all()  # Assuming you have a Category model
        brnd = Brands.objects.all()
        context = {
            'product': product,
            'brnd':brnd
        }

        if request.method == 'POST':
            name = request.POST['name']
            model = request.POST['model']
            brand_id = request.POST['brandname']
            description = request.POST['description']
            price = request.POST['price']
            kms = request.POST['kms']
            category_id = request.POST['catname']
            images = request.FILES.getlist('images')
            veh_image = request.FILES['vimage']
            catid = category.objects.get(id=category_id)
            br_id = Brands.objects.get(id=brand_id)


            vehicle = Vehicle.objects.create(
                name=name,
                brand=br_id,
                model=model,
                description=description,
                price=price,
                kms=kms,
                category=catid,
                veh_image=veh_image,
            )

            for image in images:
                VehicleImage.objects.create(
                    vehicle=vehicle, 
                    image=image)

            return redirect('index.html')  # Replace 'success_page' with the URL name of your success page

        return render(request, "sell.html", context)
    else:
        return redirect('login')



def search_items(request):
    if request.method == 'POST':
        year = request.POST.get('year')
        
        model = request.POST.get('model')
        price = request.POST.get('price')

        # Perform filtering based on the selected criteria
        items = Vehicle.objects.filter(
            year=year,
            
            model=model,
            price=price
        )

        return render(request, 'search_results.html', {'items': items})

    return render(request, 'your_search_form_template.html')





def bike_list(request):
    var = request.session.get('u_id')
    if var in request.session:
        bikes = Vehicle.objects.filter(category='2')  # Assuming you have a 'category' field in your Car model
        return render(request, 'bikes.html', {'bikes': bikes})
    else :
        return redirect('login')




def cars(request):
    var = request.session.get('u_id')
    if var in request.session:
        car_det = Vehicle.objects.filter(category='1')
        context = {
            'car_det':car_det,
        }
        return render(request,"cars.html",context)
    else:
        return redirect('login')


def car_detail(request,car_id):
    car = VehicleImage.objects.filter(vehicle=car_id)
    detail = Vehicle.objects.filter(id=car_id)
    vdet = Vehicle.objects.filter(id=car_id)
    context = {
        'car':car,
        'detail':detail,
        'vdet':vdet,
    
    }
    return render(request,"car_detail.html",context)


def userlogin(request):
    if request.method == "POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        if Regisdb.objects.filter(username=username,password=password).exists():
           data = Regisdb.objects.filter(username=username,password=password).values('name','id','phonenumber','email').first()
           request.session['name_u'] = data['name']
           request.session['u_id'] = data['id']
           request.session['phonenumber_u'] = data['phonenumber'] 
           request.session['email_u'] = data['email'] 
           request.session['username_u'] = username
           request.session['password_u'] = password
           return redirect('index.html') 
        elif User.objects.filter(username=username).exists():
            admin_details=User.objects.get(username=username)
            chek_pswd=admin_details.check_password(password)
            if chek_pswd:
                return render(request,'index-copy.html')
            else:
                return render(request,'login.html')
        else:
            return render(request,'login.html',{'msg':'invalid user credentials'})
    return render(request,'login.html')
def userlogout(request):
    del request.session['name_u']
    del request.session['u_id']
    del request.session['phonenumber_u']
    del request.session['email_u']
    del request.session['username_u']
    del request.session['password_u']
    return redirect('login')



def signup(request):
    if request.method=='POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        username = request.POST.get('username')
        phonenumber = request.POST.get('phonenumber')
        
        password = request.POST.get('password')

        Regisdb.objects.create(
            name=name,
            email=email,
            phonenumber=phonenumber,
            username=username,
            password=password

        )

    return render(request,'signup.html')

def updateprof(request):
    print("------------------------------")
    u_id = request.session['u_id']
    
    if request.method =='POST':
         
         print("------------------------------")
         name = request.POST.get('name')
         email = request.POST.get('email')
         username = request.POST.get('username')
         phonenumber = request.POST.get('phonenumber')
        
         password = request.POST.get('password')

         Regisdb.objects.filter(id=u_id).update(
            name=name,
            email=email,
            phonenumber=phonenumber,
            username=username,
            password=password
        )
    u_id = request.session['u_id']

    user = Regisdb.objects.filter(id=u_id)
    context ={
        'user_details':user
    }
    return render(request,'updateprofile.html', context)
    # return redirect('index.html')


def filtr(request,id):
    user = Regisdb.objects.filter(id=id)
    context ={
        'user':user
    }
    return render(request,"update.html",context)



            # chat views



def chat(request):
    return render(request, 'chat.html')

def room(request, room):
    username = request.GET.get('username')
    room_details = Room.objects.get(name=room)
    return render(request, 'room.html', {
        'username': username,
        'room': room,
        'room_details': room_details
    })
    

def checkview(request):
    room = request.POST['room_name']
    username = request.POST.get['username']

    if Room.objects.filter(name=room).exists():
        return redirect('/'+room+'/?username='+username)
    else:
        new_room = Room.objects.create(name=room)
        new_room.save()
        return redirect('/'+room+'/?username='+username)

def send(request):
    message = request.POST['message']
    username = request.POST['username']
    room_id = request.POST['room_id']

    new_message = Message.objects.create(value=message, user=username, room=room_id)
    new_message.save()
    return HttpResponse('Message sent successfully')

def getMessages(request, room):
    room_details = Room.objects.get(name=room)

    messages = Message.objects.filter(room=room_details.id)
    return JsonResponse({"messages":list(messages.values())})


def terms_of_service(request):
    return render(request, 'terms_of_service.html')
