from django.shortcuts import render

# Create your views here.

def login(request):
    return render(request, template_name='login.html')

def registro(request):
    return render(request, template_name='registro.html')