from django.shortcuts import render
from rest_framework.decorators import api_view
from .models import Post
from .serializers import PostSerializer
from rest_framework.response import Response
# Create your views here.

@api_view(["GET"])
def post_list(request) :
    if request.method == "GET" :
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        data = {
            "posts" : serializer.data,
            "counts" : Post.objects.count()
        }
        return Response(data)
