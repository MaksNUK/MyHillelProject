from django.db import models
from django.contrib.auth.models import User

class Group(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title

class Student(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    created_at = models.DateTimeField(auto_now_add=True)
    tags = models.ManyToManyField("core.Tags", blank=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text


class Tags(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return f"#{self.name}"