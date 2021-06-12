from django.shortcuts import render

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
