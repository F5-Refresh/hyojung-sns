from django.urls import path

from .views import PostAPIView, PostsAPIView, delete_active, like_post

urlpatterns = [
    path('', PostsAPIView.as_view()),
    path('/<int:post_id>', PostAPIView.as_view()),
    path('/<int:post_id>/delete', delete_active),
    path('/<int:post_id>/likes', like_post),
]
