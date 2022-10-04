from django.shortcuts import render

# Create your views here.
def icsmonitoringhome(request):
    return render(request, "icsmonitoring/home.html")

def plcmonitoring(request):
    return render(request, "icsmonitoring/localView.html")