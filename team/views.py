from django.shortcuts import render
from .models import team_member

def MyTeam(request):
    members=team_member.objects.all()
    context={'members':members}
    return render(request,'team/MyTeam.html',context)