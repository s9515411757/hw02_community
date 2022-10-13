from .models import Post, Group
from django.shortcuts import render, get_object_or_404

QUANTITY_POSTS = 10


def index(request):
    posts = Post.objects.order_by('-pub_date')[:QUANTITY_POSTS]
    context = {
        'posts': posts,
    }
    return render(request, 'posts/index.html', context)


def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    posts = Post.objects.filter(
        group=group
    ).order_by('-pub_date')[:QUANTITY_POSTS]

    context = {
        'group': group,
        'posts': posts,
    }
    return render(request, 'posts/group_list.html', context)
