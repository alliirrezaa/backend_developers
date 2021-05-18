from django.contrib import admin
from .models import team_member

class team_memberAdmin(admin.ModelAdmin):
    fieldsets=[
        ('profile_image', {'fields':['profile_image']})
    ]

admin.site.register(team_member)
