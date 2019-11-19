from django.shortcuts import render,redirect
from datetime import datetime
from .models import Notice,User_details
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
	context={
		'date':datetime.date(datetime.now()),
		'time':datetime.time(datetime.now())
	}
	return render(request,'webapp/home.html',context)

def details(request):
	return render(request,'webapp/details.html')

@login_required(login_url='/login/')
def information(request):
	notice = Notice.objects.all()
	context={
		'notices':notice,
	}
	return render(request,'webapp/notice.html',context)

def login(request):
	if request.method=='POST':
		username=request.POST['username']
		password=request.POST['password']

		user=auth.authenticate(username=username,password=password)

		if user is not None:
			auth.login(request,user)
			return redirect('information')
		else:
			messages.info(request,"Invalid Username and Password")
			return render(request,'webapp/login.html')

	else:
		return render(request,'webapp/login.html')

def register(request):
	if request.method=='POST':
		username=request.POST['username']
		firstname=request.POST['first_name']
		lastname=request.POST['last_name']
		email=request.POST['your_email']
		password=request.POST['password']
		confirmpassword=request.POST['comfirm_password']
		postal_code=request.POST['postalcode']
		address1=request.POST['address']

		if password==confirmpassword:
			if User.objects.filter(username=username).exists():
				messages.info(request,"Username Token!!!")
				return render(request,'webapp/register.html')

			elif User.objects.filter(email=email).exists():
				messages.info(request,"Email Token!!!")
				return render(request,'webapp/register.html')

			else:
				user=User.objects.create_user(username=username,password=password,email=email,first_name=firstname,last_name=lastname)
				userdetails=User_details(postalcode=postal_code,address=address1)
				userdetails.user=user
				user.save()
				userdetails.save()
				messages.warning(request, "Registration Completed!!!")

				return render(request,'webapp/register.html')
		else:
			messages.warning(request, "Password didn't matched!!!")
			return render(request,'webapp/register.html')

	else:
		return render(request,'webapp/register.html')


def logout(request):
	auth.logout(request)
	return redirect('index')

def fpass(request):
	if request.method=='POST':
		username=request.POST['username']
		email=request.POST['email']
		newpassword=request.POST['password2']

		user=User.objects.get(username=username)

		if user is not None:
			if email==user.email:
				user.set_password(newpassword)
				user.save()
				messages.info(request,"Password changed")
				return render(request,'webapp/change_user_pass.html')
			else:
				messages.info(request,"Email didnot matched!!!")
				return render(request,'webapp/change_user_pass.html')
		else:
			messages.info(request,"User didnot registered!!!")
			return render(request,'webapp/change_user_pass.html')



	else:
		return render(request,'webapp/change_user_pass.html')