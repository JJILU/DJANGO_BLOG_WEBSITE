from datetime import date 
from django.utils.timezone import now
from django.shortcuts import render, get_object_or_404
from django.http import Http404

from .models import Post,Author,Tag



# helper function: get post key
# def get_date(post):
#     return post['date']


# Create your views here.
def starting_page(request):
    # old way 
    # sorted_posts = sorted(posts,key=get_date)
    # latest_posts = sorted_posts[-2:]

    # new way
    latest_posts = Post.objects.all().order_by("-date")[:2]
    print(f"Time-stamp ==>> {now().timestamp()}")
    return render(request, "blog/index.html", {'timestamp': now().timestamp(),"posts":latest_posts})
    

def all_posts(request):
    posts = Post.objects.all().order_by("-date")
    return render(request, "blog/all-posts.html", {'timestamp': now().timestamp(), "all_posts":posts})
    

def post_detail(request, slug):
    # method 1
    # posts = Post.objects.all().order_by("-date")
    # identified_post = next(post for post in  posts if post.slug == slug)

    # method 2
    # identified_post = Post.objects.get(slug=slug)

    # methods 3
    identified_post = get_object_or_404(Post, slug=slug)

    
    
    if identified_post:
        omi_address = identified_post.author.email_address
        print(f"omi 6767: {omi_address}")
        return render(request, "blog/post-details.html", 
                      {
                          'timestamp': now().timestamp(), 
                          "post":identified_post,
                          "tags":identified_post.tags.all()
                      })
    else:
        raise Http404()
    
def page_404(request):
    return render(request, "blog/404.html")    