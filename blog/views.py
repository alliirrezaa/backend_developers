from django.shortcuts import render
from .models import details

def index(request):
    home_detail=details.objects.all()
    context={'home_detail':home_detail}
    return render(request,'blog/index.html',context)
