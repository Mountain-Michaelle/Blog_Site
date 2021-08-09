from django import template
from . .models import Post 


""" Starting by creating a simple tag that will retrieve
all the post """
register = template.Library() 

@register.simple_tag
def total_posts():
    return Post.objects.count()


@register.inclusion_tag('blogs/pos/latest_posts.html')
def show_latest(count=5):
    latest_posts = Post.objects.order_by('=publish')[:count]
    return{'latest_posts': latest_posts}
    


