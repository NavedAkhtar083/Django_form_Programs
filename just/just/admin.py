from django.contrib import admin

from . models import contactdata

class contactdataAdmin(admin.ModelAdmin):
    list_display=(
        'fullname',
        'email',
        'message'
        
    )

admin.site.register(contactdata,contactdataAdmin)