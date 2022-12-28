from django.urls import path

from .views import HomePageBlogs, DetailsPage

urlpatterns = [
    path('', HomePageBlogs.as_view(), name='home'),
    path('details/<int:pk>', DetailsPage.as_view(), name='details'),
]