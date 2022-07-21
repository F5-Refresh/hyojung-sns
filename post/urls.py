from django.urls import path

from .views import PostAPIView, PostsAPIView, delete_active

urlpatterns = [
    path('', PostsAPIView.as_view()),
    path('/<int:post_id>', PostAPIView.as_view()),
    path('/<int:post_id>/delete', delete_active),
]
