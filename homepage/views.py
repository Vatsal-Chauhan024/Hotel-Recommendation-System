from django.shortcuts import render

# Create your views here.
def homepage(request):
    frm = {
        'user':1
    }
    if 'username' in request.session:
        frm['user'] = 0
        
    return render(request,'homepage.html',frm)