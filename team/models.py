from django.db import models

class team_member(models.Model):
    name=models.CharField(max_length=30)
    profession=models.TextField()
    description=models.TextField()
    instagram_link=models.CharField(max_length=250)
    telegram_link=models.CharField(max_length=250)
    profile_image=models.ImageField(upload_to='%y/%m/%d',null=True,blank=True)

    def __str__(self):
        return self.name