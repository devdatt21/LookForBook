import imp
from multiprocessing.spawn import import_main_path
from django.contrib import admin
from home.models import *
from home.views import request
# Register your models here.
admin.site.register(Book_Category)
admin.site.register(Book_Deatails)
admin.site.register(SendRequest)
admin.site.register(Book_request)
admin.site.register(Send_Message)
admin.site.register(Donate_Book)
