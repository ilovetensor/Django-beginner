from django.urls import path

from .views import (
    HomePageBlogs, 
    DetailsPage, 
    CreatePost,
    UpdatePost,
    DeletePost
)

urlpatterns = [
    path('', HomePageBlogs.as_view(), name='home'),
    path('details/<int:pk>', DetailsPage.as_view(), name='details'),
    path('create_post', CreatePost.as_view(), name='post_new'),
    path('update_post/<int:pk>', UpdatePost.as_view(), name='post_update'),
    path('delete_post/<int:pk>', DeletePost.as_view(), name='post_delete'),
]