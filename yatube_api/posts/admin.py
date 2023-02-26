from django.contrib import admin

from posts.models import Group, Follow, Comment


admin.site.register(Group)
admin.site.register(Follow)
admin.site.register(Comment)
