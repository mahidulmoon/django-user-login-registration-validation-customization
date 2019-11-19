from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Notice(models.Model):
	subject=models.CharField(max_length=200)
	description=models.CharField(max_length=2000)

class User_details(models.Model):
	user=models.OneToOneField(User,on_delete=models.CASCADE)
	postalcode=models.CharField(max_length=20)
	address=models.CharField(max_length=50)


