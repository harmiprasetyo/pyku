from django.shortcuts import render, redirect

# Create your views here.

from django.http import Http404
from django.contrib import messages

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import ListView

# import class Task dari file todo/models.py
from .models import Dashboard
# import class TaskForm dari file todo/forms.py
from .forms import DashboardForm


from rest_framework import generics
from .serializers import DashboardSerializer




class DataListCreate(generics.ListCreateAPIView):
    queryset = Dashboard.objects.all()
    serializer_class = DashboardSerializer

class DataDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Dashboard.objects.all()
    serializer_class = DashboardSerializer

def index_view(request):
    # Mengambil semua data task
    dashboards = Dashboard.objects.all().order_by('-id')
   # paginate_by = 5


    paginator = Paginator(dashboards, 5)
    page = request.GET.get('page', 1)
   # posts = paginator.get_page(page_number)
 
     
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)


    

    if request.method == 'POST':
        # membuat objek dari class TaskForm
        form = DashboardForm(request.POST,initial={'username':request.user.username})
        # Mengecek validasi form
        if form.is_valid():
            # Membuat Task baru dengan data yang disubmit
            new_task = DashboardForm(request.POST)
            new_task.username = request.user.username
            # Simpan data ke dalam table tasks
            new_task.save()
            # mengeset pesan sukses dan redirect ke halaman daftar task
            messages.success(request, 'Posting anda sukses.')
            return redirect('dashboard:index')
    # Jika method-nya bukan POST
    else:
        # membuat objek dari class TaskForm
        form = DashboardForm(initial={'username':request.user.username})
    
    # memparsing data task ke template todo/index.html dan merender nya
    data = {
        'data': dashboards,
        'form':form,
        'post':posts
        
    }

    return render(request, 'dashboard/index.html', data)



def posting_view(request):
    # Mengecek method pada request
    # Jika method-nya adalah POST, maka akan dijalankan
    # proses validasi dan penyimpanan data
    if request.method == 'POST':
        # membuat objek dari class TaskForm
        form = DashboardForm(request.POST,initial={'username':request.user.username})
        # Mengecek validasi form
        if form.is_valid():
            # Membuat Task baru dengan data yang disubmit
            new_task = DashboardForm(request.POST)
            new_task.username = request.user.username
            # Simpan data ke dalam table tasks
            new_task.save()
            # mengeset pesan sukses dan redirect ke halaman daftar task
            messages.success(request, 'Posting anda sukses.')
            return redirect('dashboard:index')
    # Jika method-nya bukan POST
    else:
        # membuat objek dari class TaskForm
        form = DashboardForm(initial={'username':request.user.username})
    # merender template form dengan memparsing data form
    return render(request, 'dashboard/posting.html', {'form': form})