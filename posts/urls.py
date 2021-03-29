from django.urls import include, path
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.routers import DefaultRouter

from .views import CommentViewSet, PostViewSet


router = DefaultRouter()
router.register('posts', PostViewSet, basename='post')
router.register(r'posts/(?P<post_id>\d+)/comments', CommentViewSet,
                basename='comment')
urlpatterns = [
    path('api-token-auth/', obtain_auth_token),
    path('v1/', include(router.urls)),
]
