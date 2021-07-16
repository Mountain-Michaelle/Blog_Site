from django.shortcuts import render, get_object_or_404
from .models import Post
from django.core.paginator import Paginator, EmptyPage,\
PageNotAnInteger
from django.views.generic import ListView
from .forms import EmailPostForm
from django.core.mail import send_mail

# Create your views here.
class   PostListView(ListView):
    queryset = Post.objects.all()
    context_object_name = 'posts'
    paginate_by = 3
    template_name = 'blogs/post/list.html'


def post_share(request, post_id):
    # Retrieve post by id.
    post = get_object_or_404(Post, id=post_id, status='published')

    if request.method == 'POST':
        # form was submitted 
        form = EmailPostForm(request.POST)
        if form.is_valid():
            # form fields passed validation
            cd = form.cleaned_data
            # ... send email
            post_url = request.build_absolute_url(
                                post.get_absolute_url())
            subject = '{} ({}) recommends you reading "{}"'.format(cd['name'], cd['email'], post.title)
            massage = 'Read "{}" at {}\n\n{}\'s comments: {}'.format(post.title, post_url, cd['name'], cd['comments'])
            send_mail(subject, massage, 'mony@monycell.com', [cd['to']])
            sent = True

    else:
        form = EmailPostForm()
    context = {'post': post, 'form': form, 'sent':}
    return render(request, 'blog/post/share.html', context)




"""def post_list(request):
    object_list = Post.objects.all()
    paginator = Paginator(object_list, 3) # Three post in each page
    page = request.GET.get('page')
    try:
        posts = paginator.page(1)
    except PageNotAnInteger:
        # If page is not an integer field deliver the first page.
        posts = paginator(1)
    except EmptyPage:
        # if page is out of range deliver lase page of results
        posts = paginator.page(paginator.num_pages)
    context = {'page': page, 'posts': posts}
    return render(request,
            'blogs/post/list.html', context)"""



def post_details(request, year, month, day, post):
    post = get_object_or_404(Post, slug=post,
                                    publish__year=year,
                                    publish__month=month,
                                    publish__day=day)
    
    return render(request,
        'blogs/post/detail.html',
        {'post': post})
        