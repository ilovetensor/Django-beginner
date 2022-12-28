from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView

from .models import Post
# Create your views here.

class HomePageBlogs(ListView):
    model = Post
    template_name = 'home.html'
    

# def DetailsPage(request, pk):
#     post = get_object_or_404(Post, pk=pk)
#     return render(request, 'details.html', {'post': post})

class DetailsPage(DetailView):
    model=Post
    template_name = 'details.html'