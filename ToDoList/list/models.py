from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Task (models.Model):

    user=models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True)
    title = models.CharField(max_length=255)
    discription = models.TextField(max_length=255)
    complete=models.BooleanField(default=False)
    created=models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.title
    
    class Meta:
        ordering =['complete']

    
