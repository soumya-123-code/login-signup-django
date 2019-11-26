from django.db import models
from django.contrib.auth.models import User

class Todo(models.Model):
    fname=models.CharField(max_length=100)
    mobile=models.CharField(max_length=100)
    email=models.CharField(max_length=100)


class Post(models.Model):
    data=models.TextField()
    user=models.ForeignKey(User,on_delete=models.CASCADE)


class Comment(models.Model):
    datacomment=models.TextField()
    post=models.ForeignKey(Post,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    


    
