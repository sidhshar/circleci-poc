from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from .forms import OrganizationEnterForm
from .models import organization
import PyPDF2 as p
from django.contrib.auth.forms import UserCreationForm
# Create your views here.
def home(request):
    return render(request,'home.html')
def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = form.errors
            return render(request,'registration/signup.html',{'error':error,'f':UserCreationForm()})

    else:
        return render(request,'registration/signup.html',{ 'f':UserCreationForm()})

def upload(request):
    if request.method=="POST":
        uploaded_file=request.FILES['docy']
        #po =open(uploaded_file,'rb')
        pr = p.PdfFileReader(uploaded_file)
        helo = pr.getPage(0).extractText()
        filename=(uploaded_file.name)
        filesize=(uploaded_file.size)
        uploaded_file.close()
        return render(request, 'uploadfile.html', {'h': helo,'filename':filename,"filesize":filesize})
    return render(request,'uploadfile.html')

def createorganization(request):
    if request.method=="POST":
        form1 = OrganizationEnterForm(request.POST)
        if form1.is_valid():
            neworgc = form1.save(commit=False)
            neworgc.user = request.user
            neworgc.save()
            return redirect('home')

    else:
        form = OrganizationEnterForm()
        return render(request,'orgc/organization_create_form.html',{'form':form})

def displayorganization(request):
    org1 = organization.objects.filter(user=request.user)
    return render(request,"orgc/test.html",{'con':org1})

def editorganization(request,pid):
    orgob = get_object_or_404(organization, pk=pid)

    if request.method=="GET":
        form1 = OrganizationEnterForm(instance=orgob)
        return render(request,'orgc/editorganization.html',{'form':form1})
    else:
        form1 = OrganizationEnterForm(request.POST,instance=orgob)
        if form1.is_valid():
            form1.save()
            return redirect('displayorganization')



