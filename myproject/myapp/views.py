# myapp/views.py
from django.http import HttpResponse

def my_view(request):
    return HttpResponse("Hello from Yasin!")
