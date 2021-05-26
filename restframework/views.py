from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import status
from .models import Post
from .serializers import PostSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import permissions
# Create your views here.

@api_view(["GET"])
@permission_classes((AllowAny, ))
def post_list(request) :
    if request.method == "GET" :
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        data = {
            "posts" : serializer.data,
            "counts" : Post.objects.count()
        }
        return Response(data)



class ListPost(APIView) :
    permission_classes = [AllowAny]
    def get (self, request, format=None) :
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        data = {
            "posts": serializer.data,
            "counts": Post.objects.count()
        }
        return Response(data)

    def post (self, request) :
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid() :
            serializer.save()
            data = {
                "status" : status.HTTP_201_CREATED,
                "message" : "success",
                "data": serializer.data
            }
            return Response(data,  status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)