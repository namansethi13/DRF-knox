from django.db import models
from accounts.models import UserDetails

# Create your models here.
class Events(models.Model):
    e_id = models.AutoField(primary_key=True)
    e_name = models.CharField(max_length=200)
    e_desc = models.CharField(max_length=500,null=True)
    createdby=models.ForeignKey(UserDetails, on_delete=models.CASCADE)
    Poster=models.ImageField(upload_to='events',null=True)
    Location=models.TextField()
    start_date=models.DateField("startdate(mm/dd/yyyy)",auto_now_add=False,auto_now=False,blank=True)
    end_date=models.DateField("enddate(mm/dd/yyyy)",auto_now_add=False,auto_now=False,blank=True)
    