from datetime import date 
from django.utils.timezone import now
from django.shortcuts import render
from django.http import Http404




posts = [
            {
                "slug":"hike-in-the-mountains",
                "image":"mountains.jpg",
                "author":"Omi",
                "date": date(2025, 2,22),
                "title": "Mountain Hiking",
                "excerpt": "There's is nothig like the views when you are hiking in the mountains",
                "content": """
                            Lorem ipsum dolor sit amet consectetur adipisicing elit. Inventore tenetur, consequatur maxime itaque iste incidunt tempore. Cum minima quibusdam similique ut omnis accusamus laboriosam, nesciunt obcaecati dignissimos deleniti qui quas!

                            Lorem ipsum dolor sit amet consectetur adipisicing elit. Inventore tenetur, consequatur maxime itaque iste incidunt tempore. Cum minima quibusdam similique ut omnis accusamus laboriosam, nesciunt obcaecati dignissimos deleniti qui quas!

                            Lorem ipsum dolor sit amet consectetur adipisicing elit. Inventore tenetur, consequatur maxime itaque iste incidunt tempore. Cum minima quibusdam similique ut omnis accusamus laboriosam, nesciunt obcaecati dignissimos deleniti qui quas!
                            """
            },
            {
                "slug":"programming-is-fun",
                "image":"coding.jpg",
                "author":"James",
                "date": date(2025, 2,12),
                "title": "Programming Is Great!",
                "excerpt": "Did you ever spend trying to search for that one error in your code? if yes you are not alone!",
                "content": """
                            Lorem ipsum dolor sit amet consectetur adipisicing elit. Inventore tenetur, consequatur maxime itaque iste incidunt tempore. Cum minima quibusdam similique ut omnis accusamus laboriosam, nesciunt obcaecati dignissimos deleniti qui quas!

                            Lorem ipsum dolor sit amet consectetur adipisicing elit. Inventore tenetur, consequatur maxime itaque iste incidunt tempore. Cum minima quibusdam similique ut omnis accusamus laboriosam, nesciunt obcaecati dignissimos deleniti qui quas!

                            Lorem ipsum dolor sit amet consectetur adipisicing elit. Inventore tenetur, consequatur maxime itaque iste incidunt tempore. Cum minima quibusdam similique ut omnis accusamus laboriosam, nesciunt obcaecati dignissimos deleniti qui quas!
                            """
            },
            {
                "slug":"cooking-with-spices",
                "image":"cooking.JPG",
                "author":"Kate",
                "date": date(2025, 2,4),
                "title": "Cooking Spicy Foods",
                "excerpt": "Spices bring flavour to food turning it into a mouth-watering buffer",
                "content": """
                            Lorem ipsum dolor sit amet consectetur adipisicing elit. Inventore tenetur, consequatur maxime itaque iste incidunt tempore. Cum minima quibusdam similique ut omnis accusamus laboriosam, nesciunt obcaecati dignissimos deleniti qui quas!

                            Lorem ipsum dolor sit amet consectetur adipisicing elit. Inventore tenetur, consequatur maxime itaque iste incidunt tempore. Cum minima quibusdam similique ut omnis accusamus laboriosam, nesciunt obcaecati dignissimos deleniti qui quas!

                            Lorem ipsum dolor sit amet consectetur adipisicing elit. Inventore tenetur, consequatur maxime itaque iste incidunt tempore. Cum minima quibusdam similique ut omnis accusamus laboriosam, nesciunt obcaecati dignissimos deleniti qui quas!
                            """
            },
        ]


# helper function: get post key
def get_date(post):
    return post['date']


# Create your views here.
def starting_page(request):
    sorted_posts = sorted(posts,key=get_date)
    latest_posts = sorted_posts[-2:]
    print(f"Time-stamp ==>> {now().timestamp()}")
    return render(request, "blog/index.html", {'timestamp': now().timestamp(),"posts":latest_posts})
    

def all_posts(request):
    return render(request, "blog/all-posts.html", {'timestamp': now().timestamp(), "all_posts":posts})
    

def post_detail(request, slug):
    identified_post = next(post for post in  posts if post['slug'] == slug)
    if identified_post:
        return render(request, "blog/post-details.html", {'timestamp': now().timestamp(), "post":identified_post})
    else:
        raise Http404()
    
def page_404(request):
    return render(request, "blog/404.html")    