from django.db import models

# Create your models here.
from django.utils.translation import gettext_lazy as _
from django.db import models

class Dashboard(models.Model):
    posting = models.CharField(max_length=140)
    username = models.CharField(max_length=20)
    location = models.CharField()
    datecreate = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        db_table = "dashboard"