from django.shortcuts import render

# Create your views here.
def virus(request):
    return render(request,'virus.html')

def mm(request):
    return render(request,'mm.html')
