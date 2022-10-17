from django.shortcuts import render, get_object_or_404
from django.conf import settings

from .models import Post, Group


def index(request):
    posts = Post.objects.select_related()[:settings.QUANTITY_POSTS]
    context = {
        'posts': posts,
    }
    return render(request, 'posts/index.html', context)


def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    posts = Post.objects.filter(
        group=group
    )[:QUANTITY_POSTS]

    context = {
        'group': group,
        'posts': posts,
    }
    return render(request, 'posts/group_list.html', context)
