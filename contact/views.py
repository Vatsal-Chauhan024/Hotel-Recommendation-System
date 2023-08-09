from django.shortcuts import render

# Create your views here.
def contact(request):
    dd = {
        'user':1
    }
    if 'username' in request.session:
                dd['user'] = 0
    return render(request,'contact.html',dd)