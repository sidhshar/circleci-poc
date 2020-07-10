from django.urls import path,include
from . import views
urlpatterns = [

    path('',views.home,name='home'),
    path('signup/', views.signup, name='signup'),
    path('accounts/',include('django.contrib.auth.urls')),
    path('upload/',views.upload,name='upload'),
    path('createorganization/', views.createorganization, name='createorganization'),
    path('displayorganization/', views.displayorganization, name='displayorganization'),
    path('editorganization/<int:pid>/', views.editorganization, name='editorganization'),

]