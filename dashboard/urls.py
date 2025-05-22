from django.urls import path
from .views import index_view, posting_view, DataListCreate, DataDetail
from django.urls.conf import include



app_name = "dashboard"
urlpatterns =[
     path('', index_view, name='index'),
     path('posting', posting_view, name='posting'),
     path('home', index_view, name='home'),
     path('api/', DataListCreate.as_view(), name='apilist'),
     path('api/<int:pk>/', DataDetail.as_view(), name='apidetail'),
     

     
    



]