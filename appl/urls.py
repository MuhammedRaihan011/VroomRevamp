from django.urls import path
from appl import views



urlpatterns = [
	path('index-copy.html',views.index,name='index-copy'),
    path('addcat.html',views.addcat,name='addcat.html'),
    path('viewcat.html',views.viewcat,name='viewcat'),
    path('filters/<int:catid>',views.filters,name='filters'),
    path('dup',views.dup,name='dup'),
    path('sample',views.sample,name='sample'),
    path('delete/<int:catid>',views.delete,name='delete'),
    path('updat/<int:catid>',views.updatecat,name='updatecat'),
    path('addbrand.html',views.addbrand,name='addbrand'),
    path('view_user.html',views.view_user,name='view_user'),
    path('view_product.html',views.view_product,name='view_product'),
    path('logout',views.userlogout,name='logout'),

    
]
