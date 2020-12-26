from .views import PostList, PostDetail, PostSearch, PostListDetailfilter, CreatePost, AdminPostDetail, EditPost
#from rest_framework.routers import DefaultRouter
from django.urls import path

app_name = 'blog_api'

# router = DefaultRouter()
# router.register('', PostList, basename='post')
# urlpatterns = router.urls

urlpatterns = [
    path('post/<str:slug>', PostDetail.as_view(), name='detail-create'),
    path('search/', PostListDetailfilter.as_view(), name='post-search'),
    path('', PostList.as_view(), name='list-create'),
    path('admin/create/', CreatePost.as_view(), name='create-post'),
    path('admin/edit/post-detail/<int:pk>/', AdminPostDetail.as_view(), name='admin-detail-post'),
    path('admin/edit/<int:pk>/', EditPost.as_view(), name='edit-post')

]