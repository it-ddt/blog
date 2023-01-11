from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


app_name = "blog"
urlpatterns = [
    path("", views.PostListView.as_view(), name="index"),
    path("add", views.PostCreateView.as_view(), name="add_post"),
    path("read/<int:pk>", views.PostDetailView.as_view(), name="read_post"),
    path("delete/<int:pk>", views.PostDeleteView.as_view(), name="delete_post"),
    path("edit/<int:pk>", views.PostUpdateView.as_view(), name="edit_post"),
    path(
        "accounts/login/",
        auth_views.LoginView.as_view(template_name="blog/login.html",)
    )
]

