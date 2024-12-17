from django.contrib import admin
from enrolstu.models import datastudent
# Register your models here.
class datastudentAdmin(admin.ModelAdmin):
 list_display=('stuname','stuaddress')
 
admin.site.register(datastudent,datastudentAdmin)
