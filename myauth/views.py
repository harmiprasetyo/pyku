from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.views import LoginView, LogoutView
from django.conf import settings
from django.contrib.auth import login, authenticate
from .forms import SignUpForm
# Create your views here.
#from django.contrib.auth.views import LoginView, LogoutView


class CustomLoginView(LoginView):
	template_name = 'account/login.html';
	redirect_authenticated_user = True
	
class CustomLogoutView(LogoutView):
    template_name = 'account/login.html'
    next_page = 'login'

class RegisterView(View):
    template_name = 'account/register.html'

    def get(self, request):
        form = SignUpForm()
        return render(request, self.template_name, {'form': form})
    
    def post(self, request, *args, **kwargs):
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('login')
        
        return render(request, self.template_name, {'form': form})