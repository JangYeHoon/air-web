from django.shortcuts import render

# Create your views here.
def reservation(request):
    return render(request, 'reservation.html')

def searchList_go(request):
    return render(request, 'searchList_go.html')

def searchList_come(request):
    return render(request, 'searchList_come.html')