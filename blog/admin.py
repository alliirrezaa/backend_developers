from django.contrib import admin
from .models import details

class detailsAdmin(admin.ModelAdmin):
    fieldsets=[
        ('background_image', {'fields':['background_image']})
    ]
admin.site.register(details)
