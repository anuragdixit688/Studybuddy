from django.contrib import admin
#we have imported all the models here from models.py so that we can register here
from . models import *
# Register your models here.
admin.site.register(Room)
admin.site.register(Topic)
admin.site.register(Message)
