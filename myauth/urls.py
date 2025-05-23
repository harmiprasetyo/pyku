from django.urls import path

# import class View
from .views import CustomLoginView, CustomLogoutView, RegisterView

urlpatterns = [
    path('', CustomLoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register')
]