from django.contrib import admin
from .models import user

@admin.register(user)
class userAdmin(admin.ModelAdmin):
    list_display=('name','password','email')

# Register your models here.