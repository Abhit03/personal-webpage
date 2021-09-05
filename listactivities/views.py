from django.shortcuts import render

# Create your views here.
def photogallery(request):
    """
    Show gallery view 
    """
    return render(request, "listactivities/gallery.html")