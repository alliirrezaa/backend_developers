from django.urls import path
from . import views

app_name='team'
urlpatterns=[
    path('MyTeam/',views.MyTeam,name='MyTeam')
]