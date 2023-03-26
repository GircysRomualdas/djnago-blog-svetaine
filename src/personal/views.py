from django.shortcuts import render
from operator import attrgetter
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

from blog.views import get_blog_queryset
from blog.models import BlogPost


BLOG_POSTS_PER_PAGE = 7


# ! shows home page (request is request made to server)
def home_screen_view(request):

    context = {}

    query = ""
    if request.GET:
        query = request.GET.get('q', '')
        context['query'] = str(query)
    
    blog_posts = sorted(get_blog_queryset(query), key=attrgetter('date_updated'), reverse=True)

    # Pagination
    page = request.GET.get('page', 1)
    blog_posts_paginator = Paginator(blog_posts, BLOG_POSTS_PER_PAGE)

    try:
        blog_posts = blog_posts_paginator.page(page)
    except PageNotAnInteger:
        blog_posts = blog_posts_paginator.page(BLOG_POSTS_PER_PAGE)
    except EmptyPage:
        blog_posts = blog_posts_paginator.page(blog_posts_paginator.num_pages)




    recent_view_blog = None
    # Session
    try:
        recent_view_blog = request.session['visited']
    except:
        recent_view_blog = None

    context = {
        'blog_posts': blog_posts,
        'recent_view_blog': recent_view_blog,
    }

    return render(request, "personal/home.html", context)
