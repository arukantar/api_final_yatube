<<<<<<< HEAD
from django.urls import include, path
from rest_framework.routers import DefaultRouter
from api.views import PostViewSet, GroupViewSet, CommentViewSet, FollowViewSet

v1_router = DefaultRouter()
v1_router.register('posts', PostViewSet)
v1_router.register('groups', GroupViewSet)
v1_router.register(
    r'^posts/(?P<post_id>\d+)/comments', CommentViewSet, basename='comments'
)
v1_router.register('follow', FollowViewSet, basename='follow')

urlpatterns = [
    path('v1/', include('djoser.urls')),
    path('v1/', include('djoser.urls.jwt')),
    path('v1/', include(v1_router.urls)),
=======
from django.urls import path

urlpatterns = [
>>>>>>> 000fc00ccec8453459136e5c568055db8a7294f0
]
