from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView, get_object_or_404
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from .models import Post
from .serializers import PostSerializer, PostDetailSerializer


class ListPostView(ListCreateAPIView):
    # 00-00 post 리스트 전체 조회
    # 00-01 post 생성
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    list_serializer_class = PostSerializer
    create_serializer_class = PostDetailSerializer


class DetailPostView(APIView):
    # 00-02 post 상세 조회
    def get(self, request, pk):
        post = get_object_or_404(Post, id=pk)
        serializer = PostDetailSerializer(post)
        return Response(serializer.data, status=HTTP_200_OK)

    # 00-03 post 수정
    def put(self, request, pk):
        post = get_object_or_404(Post, id=pk)
        serializer = PostDetailSerializer(post, data=request.data, partial=True)
        if serializer.is_valid():
            updated_post = serializer.save()
            serializer = PostDetailSerializer(updated_post)
            return Response(serializer.data, status=HTTP_200_OK)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

    """
    작성자만 삭제할 수 있도록 구현
    def delete(self, request):
        post = get_object_or_404(Post, id=pk)
    """