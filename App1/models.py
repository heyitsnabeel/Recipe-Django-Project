from django.db import models
from django.contrib.auth.models import User
from rest_framework import serializers

# Create your models here.
class Recipe(models.Model):
    user = models.ForeignKey(User,on_delete=models.SET_NULL,null=True,blank=True)
    name = models.CharField(max_length=100)
    description = models.TextField()
    review = models.TextField()

class folder(models.Model):
    first_name = models.CharField(max_length=100)    
    last_name = models.CharField(max_length=100)    
    description = models.TextField(max_length=400)    

from django.contrib.auth.models import Group, User
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']
