from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
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

class CreatePost(CreateView):
    model = Post
    template_name = 'create.html'
    fields = ['title', 'author', 'body']

class UpdatePost(UpdateView):
    model = Post
    fields = ['title', 'body']
    template_name='update_post.html'

class DeletePost(DeleteView):
    model = Post
    template_name = 'delete.html'
    success_url = reverse_lazy('home')
