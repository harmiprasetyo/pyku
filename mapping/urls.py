from django.urls import path
from .views import map_view
app_name = "mapping"
urlpatterns =[
     path('', map_view, name='mapping'),
     path('map', map_view, name='map'),
    
    
]