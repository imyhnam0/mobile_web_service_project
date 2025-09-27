from django.shortcuts import render
from .models import Post

def post_list(request):
    posts = Post.objects.order_by('-published_date', '-created_date')
    return render(request, 'blog/post_list.html', {'posts': posts})


from rest_framework import viewsets
from .serializers import PostSerializer

class BlogImage(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

