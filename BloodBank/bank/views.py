from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from .models import UserProfile,BloodStock
# Create your views here.

def index(request):
    if request.method == 'POST':
        city = request.POST['city']
        bloodgr = request.POST['bloodgroup']
        users = UserProfile.objects.filter(City=city, Blood_group=bloodgr)
        return render(request, 'bank/search.html',{'users':users})
    else:
        return render(request, 'bank/index.html')

def bloodTips(request):
    return render(request, 'bank/bloodTips.html')

def reg(request):
    if request.method == 'POST':
        first_name = request.POST['firstname']
        last_name = request.POST['lastname']
        gender = request.POST['gender']
        dob = request.POST['dob']
        email = request.POST['email']
        password = request.POST['password']
        contact = request.POST['contact']
        city = request.POST['city']
        state = request.POST['state']
        zip1 = request.POST['zip']
        bloodgr = request.POST['bloodgroup']
        username = request.POST['email']
        user=User.objects.create_user(username=username,password=password,email=email,first_name=first_name,last_name=last_name)
        user.save()
        userp=UserProfile(user=user, Mobile=contact, Gender=gender, Dob=dob, Blood_group=bloodgr, City=city, State=state, Zip_code=zip1)
        userp.save()
        return redirect('login')
    else:
        return render(request, 'bank/register.html')

def login(request):
    if(request.method == 'POST'):
        username = request.POST['email']
        password = request.POST['password']
        user=auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('home')
        else:
            return redirect('login')
    else:
        return render(request, 'bank/login.html')

def logout(request):
    auth.logout(request)
    return redirect('home')

def about(request):
    return render(request, 'bank/aboutus.html')

def donate(request):
    if request.method == 'POST':
        amt = int(request.POST['amount'])
        username = request.POST['user']
        user = User.objects.get(username=username)
        userP = UserProfile.objects.get(user=user)
        userP.Blood_Donated = userP.Blood_Donated + amt
        userP.save()
        bs = BloodStock.objects.get(Blood_group=userP.Blood_group)
        bs.Blood_Stock = bs.Blood_Stock + amt
        bs.save()
        return redirect('home')
    else:
        return render(request, 'bank/donate.html')
