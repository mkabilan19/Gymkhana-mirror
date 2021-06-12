from django.shortcuts import render,redirect
from . import forms
from .models import Complaints

# Create your views here.
def home(request):
    return render(request,'common.html')


def HAB(request):
    return render(request, 'hab.html')


def technical(request):
    return render(request, 'technical.html')


def sports(request):
    return render(request, 'sports.html')


def senate(request):
    return render(request, 'senate.html')


def welfare(request):
    return render(request, 'welfare.html')


def cultural(request):
    return render(request, 'cultural.html')


def complaint(request):
    if request.method == 'POST':
        form = forms.ComplaintForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = forms.ComplaintForm()
    return render(request, 'complaint.html', {'form': form})
