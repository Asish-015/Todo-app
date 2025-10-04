from django.contrib import admin
from app import models
from .models import TODO,signup

admin.site.register(TODO)
admin.site.register(signup)
# Register your models here.
