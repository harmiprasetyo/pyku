from django.forms import ModelForm
from django import forms
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
# import class Task dari file todo/models.py
from .models import Dashboard
import datetime

from django.core.validators import RegexValidator
# membuat class TaskForm untuk membuat task
class DashboardForm(ModelForm):
    
    

    class Meta:
        # mereladsikan form dengan model
        model = Dashboard
        # mengeset field apa saja yang akan ditampilkan pada form
        fields = ('posting', 'datecreate', 'location','username')
        # mengatur teks label untuk setiap field
        labels = {
            'posting': _('Posting'),
            'datecreate': _('Tanggal'),
            'location': _('Lokasi')
        }

       
        # mengatur teks pesan error untuk setiap validasi fieldnya
        error_messages = {
            'posting': {
                'required': _("Harus diisi!!"),
                
            },
            
        }
       
       # username = request.user.username
    
        widgets ={
            'posting': forms.TextInput(attrs={'class':"form-control"}),
            'username': forms.HiddenInput(),
            'location': forms.HiddenInput(attrs={"value":"@here"}),
            'datecreate':forms.HiddenInput(attrs={"value": datetime.date.today().strftime("%Y-%m-%d")})
        }