from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from django.conf import settings

from .models import Post, Group, User


def index(request):
    post_list = Post.objects.all()
    paginator = Paginator(post_list, settings.QUANTITY_POSTS)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,

    }
    return render(request, 'posts/index.html', context)


def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    posts = Post.objects.filter(
        group=group
    )[:settings.QUANTITY_POSTS]

    context = {
        'group': group,
        'posts': posts,
    }
    return render(request, 'posts/group_list.html', context)


def profile(request, username):
    user = User.objects.get(username=username)
    # Здесь код запроса к модели и создание словаря контекста
    post_list = Post.objects.filter(author = user)
    paginator = Paginator(post_list, settings.QUANTITY_POSTS)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    username = user.get_full_name

    context = {
        'page_obj': page_obj,
        'post_list': post_list,
        'username': username,
    }
    return render(request, 'posts/profile.html', context)


def post_detail(request, post_id):
    # Здесь код запроса к модели и создание словаря контекста
    post = Post.objects.get(
        pk=post_id
    )
    user = User.objects.get(username=post.author)
    post_count = Post.objects.filter(author=user)
    context = {
        'post': post,
        'post_count': post_count,
    }
    return render(request, 'posts/post_detail.html', context)