from django.shortcuts import render

# Create your views here.
def tranfusionsHome(request):
    return render(request, 'tranfusion.html')