from django.urls import path

from .views import HomePageBlogs, DetailsPage, CreatePost

urlpatterns = [
    path('', HomePageBlogs.as_view(), name='home'),
    path('details/<int:pk>', DetailsPage.as_view(), name='details'),
    path('create_post', CreatePost.as_view(), name='post_new'),
]