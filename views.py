from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.urls import reverse, reverse_lazy
from django.contrib.auth import authenticate
from django.views.generic import ListView, CreateView, DeleteView, UpdateView, DetailView
from .models import Post
from .forms import LoginForm
"""
TODO: реализовать аутентификацию пользователя (логин, логоут, востт пасса, регистрацию)
с помощью auth_views
"""


class PostDetailView(DetailView):
    model = Post


class PostListView(ListView):
    model = Post


class PostCreateView(CreateView):
    model = Post
    fields = "__all__"
    success_url = reverse_lazy("blog:index")


class PostDeleteView(DeleteView):
    model = Post
    success_url = reverse_lazy("blog:index")


class PostUpdateView(UpdateView):
    model = Post
    fields = "__all__"
    success_url = reverse_lazy("blog:index")
    template_name_suffix = '_update_form'


def login(request):
    if request.method == "GET":
        data = {"form": LoginForm()}
        return render(request, 'blog/login.html', data)
    else:
        form = LoginForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data["name"]
            password = form.cleaned_data["password"]
            is_authorized = authenticate(username=name, password=password)
            if is_authorized:
                return HttpResponse(f"Пользователь {name} авторизован")
            else:
                return HttpResponse(f"Не удалось авторизовать пользователя {name}")
        else:
            return HttpResponse("Форма невалидна")
