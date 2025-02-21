from django.utils.timezone import now
from django.shortcuts import render

# Create your views here.
def starting_page(request):
    print(f"Time-stamp ==>> {now().timestamp()}")
    return render(request, "blog/index.html", {'timestamp': now().timestamp()})
    

def posts(request):
    return render(request, "blog/all-posts.html", {'timestamp': now().timestamp()})
    

def post_detail(request, slug):
    return render(request, "blog/post-details.html", {'timestamp': now().timestamp()})