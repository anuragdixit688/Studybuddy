from django.forms import ModelForm
from .models import *
from django.contrib.auth.models import User

class RoomForm(ModelForm):
    class Meta:
        model= Room
        fields = '__all__' #we can render all models fields
        exclude = {'host','members'} #so that these two fields
        # are excluded and will be taken care of by the backend

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['username','email']


