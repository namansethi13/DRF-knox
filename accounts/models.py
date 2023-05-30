from django.db import models
from django.contrib.auth.models import User
from .collegeChoice import collegesTup

SEMESTER_CHOICES = (
    ("1", "1"),
    ("2", "2"),
    ("3", "3"),
    ("4", "4"),
    ("5", "5"),
    ("6", "6"),
    ("7", "7"),
    ("8", "8"),
)

# Create your models here.
class UserDetails(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_details')
    college = models.CharField(choices=collegesTup, max_length=200 , blank=True , null= True )
    semester = models.CharField(
        max_length = 20,
        choices = SEMESTER_CHOICES,
        default = '1'
        )
    is_college_amabassador = models.BooleanField(default=False) 
    bio = models.CharField( max_length=500, null=True, blank=True)
    is_email_verified = models.BooleanField()
    profile_picture=models.ImageField(upload_to='profpictures',null=True)
    def __str__(self):
        return "%s" %(self.user)

 

    