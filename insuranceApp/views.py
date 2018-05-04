from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Profile,Product

# view function for main page
def index(request):
    product=Product.objects.all()
    return render (request,'index.html',{"product":product})


# view function for a single user profile
def profile(request,user_id):

    profiles= Profile.objects.get(id = user_id)
    return render (request ,'profile.html',{"profiles":profiles})
