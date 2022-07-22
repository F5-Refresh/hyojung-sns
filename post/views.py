from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, status
from rest_framework.decorators import api_view
from rest_framework.generics import GenericAPIView, get_object_or_404
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.response import Response
from rest_framework.views import APIView

from post.serializers import PostsSerializer

from .models import Post


class PostsAPIView(GenericAPIView):

    queryset = Post.objects.all()
    serializer_class = PostsSerializer

    # filter, search, ordering
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['hashtag']
    search_fields = ['title']
    ordering_fields = ['created_at', 'likes', 'hits']
    ordering = ['created_at']

    # pagination
    pagination_class = LimitOffsetPagination

    def get(self, request):
        posts = Post.objects.all()
        filtered_posts = self.filter_queryset(posts)
        page = self.paginate_queryset(posts)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = PostsSerializer(filtered_posts, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        # hashtag = request.data['hashtag'].split(',')
        serializer = PostsSerializer(data={"writer": request.user.id, **request.data})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PostAPIView(APIView):
    def get(self, request, post_id):
        post = get_object_or_404(Post, id=post_id)
        hits = post.hits + 1
        serializer = PostsSerializer(post, data={"hits": hits}, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def patch(self, request, post_id):
        post = get_object_or_404(Post, id=post_id)
        serializer = PostsSerializer(post, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PATCH'])
def delete_active(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    post.toggle_active()
    return Response(post.delete_message, status=status.HTTP_200_OK)


@api_view(['GET'])
def like_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)

    if request.user in post.likes.all():
        post.likes.remove(request.user.id)
        message = "좋아요 취소!"
    else:
        post.likes.add(request.user.id)
        message = "좋아요 등록!"

    return Response({"message": message})
