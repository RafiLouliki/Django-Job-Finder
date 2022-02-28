from .models import Post,Comment
from .serializers import PostSerializer,CommentSerializer
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.decorators import api_view

# Create your views here.

#Generic Based Views

class Post_ListApi(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class Post_DetailApi(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    lookup_field = 'id'
    

class Comment_ListApi(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class Comment_DetailApi(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()
    lookup_field = 'id'




#End Of Generic Class Based Views



#Function Based Views
@api_view(['GET'])
def Post_list_func_api(request):
    all_Post = Post.objects.all()
    data = PostSerializer(all_Post, many=True).data
    return Response({'data':data})


@api_view(['GET'])
def Post_detail_func_api(request,id):
    Post_detail = Post.objects.get(id=id)
    data = PostSerializer(Post_detail).data
    return Response({'data':data})


@api_view(['GET'])
def Comment_list_func_api(request):
    all_Comment = Comment.objects.all()
    data = CommentSerializer(all_Comment, many=True).data
    return Response({'data':data})



@api_view(['GET'])
def Comment_detail_func_api(request,id):
    Comment_detail = Comment.objects.get(id=id)
    data = CommentSerializer(Comment_detail).data
    return Response({'data':data})




#ُEnd Fuction Based Views Api



