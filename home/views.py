from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request, 'index.html')




def add(request):
    value1 = request.POST['num1']
    value2 = request.POST['num2']
    result = int(value1) + int(value2)
    return render(request, 'result.html', {'base': 'base.html', 'res': result})
