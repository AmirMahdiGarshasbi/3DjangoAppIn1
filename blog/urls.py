from django.urls import path

from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView

urlpatterns = [
    path("blog/", PostListView.as_view(), name='post-list'),
    path("blog/<int:pk>/", PostDetailView.as_view(), name='post-detail'),
    path("blog/new/", PostCreateView.as_view(), name='post-new'),
    path("blog/<int:pk>/edit/", PostUpdateView.as_view(), name='post-edit'),
    path("blog/<int:pk>/delete/", PostDeleteView.as_view(), name='post-delete'),
]