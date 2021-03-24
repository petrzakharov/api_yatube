from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.routers import DefaultRouter

from .views import PostViewSet, CommentViewSet

router = DefaultRouter()
router.register('v1/posts', PostViewSet, basename='post')
router.register(r'v1/posts/(?P<id>\d+)/comments', CommentViewSet,
                basename='comment'
                )
urlpatterns = [
    path('v1/api-token-auth/', obtain_auth_token),
    path('', include(router.urls)),
]
