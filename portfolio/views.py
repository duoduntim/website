from django.shortcuts import render
from . models import Projects,Education,skills,programs,experience
from  django.http import HttpResponse
from django.core.mail import send_mail
# Create your views here.
def index(request):
    return render(request,'core/index.html')

def resume(request):
    education = Education.objects.all()
    Skills=skills.objects.all()
    Experience=experience.objects.all()
    Programs=programs.objects.all()
    return render(request,'core/resume.html',{'all':education,'eve':Skills,'ing':Experience,'evg':Programs})

def projects(request):
    all_members= Projects.objects.all
    return render (request,'core/projects.html',{'all':all_members})
def contact(request):
    if request.method ==  "POST":
        sub = request.POST.get('subject')
        msg = request.POST.get('message')
        email = request.POST.get('email')
        print(sub,msg,email)
        return HttpResponse('email sent')
        send_mail{
            sub,msg,'kwabsntim@gmail.com'
            [email]
        }

    return render (request,'core/cont.html')