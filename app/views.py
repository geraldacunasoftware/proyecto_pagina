from django.shortcuts import render
from django.utils.translation import gettext as _

# Create your views here.
def index(request):
    return render(request,'index.html')
