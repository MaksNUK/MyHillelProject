from django.contrib import admin
from .models import Group, Student, Post, Comment, Tags

admin.site.register(Group)
admin.site.register(Student)
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Tags)

# Register your models here.
