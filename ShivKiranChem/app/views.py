from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse('Om Shanti! <br> Mera Baba, Pyara Baba, Bhole Baba, Methe Baba...')