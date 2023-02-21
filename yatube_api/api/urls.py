from django.urls import include, path
from rest_framework.routers import SimpleRouter

from api.views import (
    CommentViewSet, GroupViewSet, PostViewSet, UserViewSet, FollowViewSet
)


router_v1 = SimpleRouter()

router_v1.register('posts', PostViewSet, basename='posts')
router_v1.register('users', UserViewSet, basename='users')
router_v1.register('groups', GroupViewSet, basename='groups')
router_v1.register('posts', PostViewSet, basename='posts')
router_v1.register('follow', FollowViewSet, basename='follow')
router_v1.register(
    r'posts/(?P<post_id>\d+)/comments',
    CommentViewSet,
    basename='comments',
)

urlpatterns = [
    path('v1/', include(router_v1.urls)),
    path('v1/auth/', include('djoser.urls')),
    path('v1/', include('djoser.urls.jwt')),
]
