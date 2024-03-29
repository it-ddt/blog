from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import logout
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.conf import settings
from .models import Post, Category, Like

class PostDetailView(DetailView):
    model = Post

class PostListView(ListView):
    model = Post

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['MEDIA_URL'] = settings.MEDIA_URL
        return context

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'text', 'category', 'image']
    success_url = reverse_lazy('blog:post_list')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UpdateView):
    model = Post
    fields = ['title', 'text', 'category']

class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    success_url = '/posts/'

class CategoryDetailView(DetailView):
    model = Category

class CategoryListView(ListView):
    model = Category

def add_like(request, pk):
    post = get_object_or_404(Post, pk=pk)
    like = Like(user=request.user, post=post)
    like.save()
    return redirect('blog:post_detail', pk=pk)

def remove_like(request, pk):
    post = get_object_or_404(Post, pk=pk)
    like = Like.objects.get(user=request.user, post=post)
    like.delete()
    return redirect('blog:post_detail', pk=pk)

def logout_view(request):
    logout(request)
    return redirect('blog:post_list')