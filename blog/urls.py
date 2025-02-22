from django.urls import path

from . import views


urlpatterns = [
    path("", views.starting_page, name="starting-page"),
    path("posts", views.all_posts, name="posts-page"),
    path("posts/<slug:slug>", views.post_detail, name="posts-details-page"),  #/post/my-first-post
    path("404", views.page_404, name="post-not-found")
]
