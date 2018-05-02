from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Profile


def index(request):
    return render (request,'index.html')

# Create your views here.

def profile(request,user_id):

    profiles= Profile.objects.get(id = user_id)
    return render (request ,'profile.html',{"profiles":profiles})
