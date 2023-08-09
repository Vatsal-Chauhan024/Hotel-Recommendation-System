from django.shortcuts import render,redirect
from .models import User_sign

def sign_up(request):
    dict={}
    if request.method == "POST":
        username = request.POST['userid']
        password = request.POST['password'] 
        phonenumber = request.POST['phonenumber']
        userid = list(User_sign.objects.values_list('user_name', flat = True))
        if username in userid :
            dict.update({"Error":"Already Registered."})
            return render(request,'sign-up.html',dict)
        
        login = User_sign()
        login.user_name = username
        login.password = password
        login.phone_number = phonenumber
        login.save()
        request.session['username'] = username
        return redirect('/') 
    return render(request,'sign-up.html')




def log_in(request):
    if(request.method == "POST"):
        userid = list(User_sign.objects.values_list('user_name', flat = True))
        password = list(User_sign.objects.values_list('password', flat = True))
        user_id = request.POST['userid']
        dict={}
        user_password = request.POST['password']
        if user_id in userid:
            
            if user_password == password[userid.index(user_id)]:
                # dict.update({'username':user_id})
                request.session['username'] = user_id
                return redirect('/')
            else:
                dict.update({"Error":"UserId/Password Invalid"})
                return render(request,'sign_in.html',dict)
    return render(request,'sign_in.html')

