from django.urls import path

# import my_view from todo Application
from .views import index_view, detail_view, create_view, update_view, delete_view
app_name = 'todo'
urlpatterns = [
    path('', index_view, name='index'),
    	# route untuk halaman detail task
    path('<int:task_id>', detail_view, name='detail'),
      # url untuk halaman tambah task
    path('create', create_view, name='create'),
        # url untuk halaman ubah task
    path('update/<int:task_id>', update_view, name='update'),
        # url untuk menghapus task
    path('delete/<int:task_id>', delete_view, name='delete'),
]