from django.urls import path
from .views import HomePageView
# write your urls here

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
]