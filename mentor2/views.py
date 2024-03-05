from django.shortcuts import render,redirect
from mentor2.models import Member


# Create your views here.
def about(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contact.html')


def index(request):

    return render(request, 'index.html')


def register(request):
    if request.method == 'POST':
        member = Member(username=request.POST['username'], email=request.POST['email'],password=request.POST['password'])
        member.save()
        return redirect('/login')
    else:
        return render(request, 'register.html')



def login(request):
    if request.method == 'POST':
        if Member.objects.filter(username=request.POST['username'],password=request.POST['password']).exists():
            member = Member.objects.get(username=request.POST['username'],password=request.POST['password'])

            return render(request, 'index.html',{'member':member})
        else:
            return render(request, 'login.html')

    else:
        return render(request, 'login.html')
