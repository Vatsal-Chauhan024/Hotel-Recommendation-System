from django.shortcuts import render

def about(request):
    dd = {
        'user':1
    }
    if 'username' in request.session:
                dd['user'] = 0
    return render(request,'about.html',dd)