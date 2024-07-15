from django.shortcuts import render,redirect
from django.core.paginator import Paginator
from django.http import HttpResponse
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required(login_url="/login/")
def recipe(request):
    if request.method=="POST":
        data = request.POST
        name = data.get('name')
        description = data.get('description')
        review = data.get('review')

        Recipe.objects.create(
            name=name,
            description=description,
            review=review,
            )
        return redirect("/recipe/")
    
    queryset = Recipe.objects.all()
    context = {'recipies':queryset}

    return render(request,"index.html",context)

def delete_recipe(request,id):
    queryset = Recipe.objects.get(id=id)
    queryset.delete()
    return redirect("/recipe/")

def update_recipe(request,id):
    queryset = Recipe.objects.get(id=id)
    if request.method=='POST':
        data = request.POST

        name = data.get('name')
        description = data.get('description')
        review = data.get('review')

        queryset.name = name
        queryset.description = description
        queryset.review = review

        queryset.save()
        return redirect("/recipe/")
    
    context = {'recipe':queryset}
    return render(request,'update.html',context)

def login_page(request):

    if request.method=="POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        if not User.objects.filter(username=username).exists():
            return redirect('/login/')
        
        user = authenticate(username=username,password=password)

        if user is None:
            return redirect('/login/')
        
        else:
            login(request,user)
            return redirect("/recipe/")

    return render(request,'login.html')

def logout_page(request):
    logout(request)
    return redirect('/login/')


def register_page(request):
    if request.method=="POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = User.objects.filter(username=username)

        if user.exists():
            return redirect('/register/')

        user = User.objects.create(
            first_name=first_name,
            last_name=last_name,
            username=username
        )
        user.set_password(password)
        user.save()
        return redirect('/register/')


    return render(request,'register.html')

from django.contrib.auth.models import Group, User
from rest_framework import permissions, viewsets  
#from tutorial.quickstart.serializers import GroupSerializer, UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all().order_by('name')
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]