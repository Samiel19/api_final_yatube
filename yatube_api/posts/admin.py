from django.contrib import admin

from posts.models import Group, Follow, Comment, Post


admin.site.register(Group)
admin.site.register(Post)
admin.site.register(Follow)
admin.site.register(Comment)
