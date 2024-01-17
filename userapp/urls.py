from django.urls import path
from userapp import views

urlpatterns = [
    path('index.html',views.index,name='index.html'),
    path('sell.html',views.sell,name='sell.html'),
    path('bikes',views.bike_list,name='bikes'),
    path('cars.html',views.cars,name='cars.html'),
    path('car_detail/<int:car_id>', views.car_detail, name='car_detail'),
    path('signup/',views.signup,name='signup'),
    path('login',views.userlogin,name='login'),
    path('logout',views.userlogout,name='logout'),
    path('updateprof/',views.updateprof,name='updateprof'),
    path('filtr/<int:id>',views.filtr,name='filtr'),
    path('search/', views.search_items, name='search_items'),
    
    
    path('chat', views.chat, name='chat'),
    path('room/<str:room>/', views.room, name='room'),
    path('checkview', views.checkview, name='checkview'),
    path('send', views.send, name='send'),
    path('getMessages/<str:room>/', views.getMessages, name='getMessages'),

]
