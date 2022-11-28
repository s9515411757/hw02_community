from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.core.paginator import Paginator
from django.conf import settings
from django.contrib.auth.decorators import login_required

from .models import Post, Group, User
from .forms import PostForm


@login_required
def index(request):
    post_list = Post.objects.all()
    paginator = Paginator(post_list, settings.QUANTITY_POSTS)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,

    }
    return render(request, 'posts/index.html', context)


@login_required
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


@login_required
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


@login_required
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


@login_required
def post_create(request):
    form = PostForm(request.POST or None)
    if form.is_valid():
        form = form.save(commit=False)
        form.author = request.user
        form.save()
        return redirect('posts:profile', request.user.username)
    template = 'posts/create_post.html'
    context = {'form': form,
               'is_edit': False}
    return render(request, template, context)


def post_edit(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    form = PostForm(instance=post)

    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.author = request.user
            form.save()
            return redirect('posts:profile', request.user.username)

    template = 'posts/create_post.html'

    context = {
       'is_edit': True,
       'form': form,

    }
    return render(request, template, context)

