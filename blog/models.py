from django.db import models

class details(models.Model):
    name=models.CharField(max_length=30)
    info_1=models.TextField()
    info_2=models.TextField()
    background_image=models.ImageField(upload_to='%y/%m/%d',null=True,blank=True)


    def __str__(self):
        return self.name