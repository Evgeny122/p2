from django.shortcuts import render

def index(request):
    data = [i for i in range(10)]
    return render(request, 'index.html', {'test_data' : data})