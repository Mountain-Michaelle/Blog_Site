from django import template
from django.db.models import Count
from . .models import Post 


""" Starting by creating a simple tag that will retrieve
all the post """
register = template.Library() 

@register.simple_tag
def total_posts():
    return Post.objects.count()

@register.simple_tag
def get_most_commented_posts(count=5):
    return Post.objects.annotate(
        total_comments=Count('comments')
    ).order_by('-total_comments')[:4]


@register.inclusion_tag('blogs/post/latest_posts.html')
def show_latest_posts(count=5):
    latest_posts = Post.objects.order_by('-publish')[:3]
    return{'latest_posts': latest_posts}
    


