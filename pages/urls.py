from django.urls import path
from . import views
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, UserPostListView
from django.contrib.auth.decorators import login_required


urlpatterns = [
    path('', login_required(PostListView.as_view()),name="home"),
    path('posts/<str:username>/', UserPostListView.as_view(), name="user_posts"),
    path('post/<int:pk>', PostDetailView.as_view(), name="post"),
    path('post/create', PostCreateView.as_view(), name="create"),
    path('post/<int:pk>/update', PostUpdateView.as_view(), name="update"),
    path('post/<int:pk>/delete', PostDeleteView.as_view(), name="delete"),
    
    
]
