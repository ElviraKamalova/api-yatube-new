from django.urls import include, path
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.routers import DefaultRouter
from api.views import PostViewSet, GroupViewSet, CommentViewSet

router = DefaultRouter()
router.register(r'api/v1/posts', PostViewSet, basename='post')
router.register(r'api/v1/groups', GroupViewSet, basename='group')
router.register(
    r'api/v1/posts/(?P<post_id>\d+)/comments',
    CommentViewSet,
    basename='comment'
)

urlpatterns = [
    path('', include(router.urls)),
    path('api/v1/api-token-auth/', obtain_auth_token, name='api_token_auth')
]
