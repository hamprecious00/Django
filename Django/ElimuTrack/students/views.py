from django.shortcuts import render
from .models import Student
from django.http import HttpResponseRedirect

# Create your views here.
def index(request):
    return render(request, 'students/index.html',
                  {'students': Student.objects.all()})
