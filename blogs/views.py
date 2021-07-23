from django.shortcuts import render, get_object_or_404
from .models import Post, Comment
from django.core.paginator import Paginator, EmptyPage,\
PageNotAnInteger
from django.views.generic import ListView
from .forms import EmailPostForm, CommentForm
from django.core.mail import send_mail

# Create your views here.
class   PostListView(ListView):
    queryset = Post.objects.all()
    context_object_name = 'posts'
    paginate_by = 3
    template_name = 'blogs/post/list.html'


def post_share(request, post_id):
    # Retrieve post by id.
    post = get_object_or_404(Post, id=post_id)
    sent = False

    
    if request.method == 'POST':
        # form was submitted 
        form = EmailPostForm(request.POST)
        if form.is_valid():
            # form fields passed validation
            cd = form.cleaned_data
            # ... send email
            post_url = request.build_absolute_uri(
                                post.get_absolute_url())
            subject = '{} ({}) recommends you reading "{}"'.format(cd['name'], cd['email'], post.title)
            massage = 'Read "{}" at {}\n\n{}\'s comments: {}'.format(post.title, post_url, cd['name'], cd['comments'])
            send_mail(subject, massage, 'mony@monycell.com', [cd['to']])
            sent = True

    else:
        form = EmailPostForm()
    context = {'post': post, 'form': form, 'sent': sent}
    return render(request, 'blogs/share.html', context)




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
    
    # list of active comments for this post
    comments = post.comments.filter(active=True)
    new_comment = None

    if request.method == 'POST':
        # A comment was posted
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid:
            # create comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.post = post
            # save the post to the database.
            new_comment.save()
    else:
        comment_form = CommentForm()
    context = {'post':post, 'comments':comments, 'new_comment': new_comment, 
    'comment_form': comment_form}
    return render(request, 'blogs/post/detail.html', context)                