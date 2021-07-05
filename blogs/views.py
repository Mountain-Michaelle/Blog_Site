from django.shortcuts import render, get_object_or_404
from .models import Post

# Create your views here.

def post_list(request):
    posts = Post.objects.all()
    return render(request,
            'blogs/post/list.html',
            {'posts': posts })

def post_details(request, year, month, day, post):
    post = get_object_or_404(Post, slug=post,
                                    publish__year=year,
                                    publish__month=month,
                                    publish__day=day)
    
    return render(request,
        'blogs/post/detail.html',
        {'post': post})
        