from django.urls import path
from rest_framework.routers import SimpleRouter
from .views import UsersViewSet, PostViewSet
# from .views import PostDetail, PostList, UserList, UserDetail

# urlpatterns = [
#     path('', PostList.as_view()),
#     path('<int:pk>/', PostDetail.as_view()),
#     path('users/', UserList.as_view()),
#     path('users/<int:pk>/', UserDetail.as_view()),
# ]

router = SimpleRouter()
router.register('users', UsersViewSet, basename='users')
router.register('', PostViewSet, basename='posts')
urlpatterns = router.urls
