from rest_framework import viewsets

from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, redirect, get_object_or_404

from .forms import PostForm
from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

def main_spa(request, page = 1):
    posts = Post.objects.all().order_by("-created_at")
    print(posts)
    # робота з пагiнатором
    elem_per_page = 5
    paginator = Paginator(posts, elem_per_page)
    posts_on_page = paginator.page(page)
    print(posts_on_page)
    return render(request, "spa/main_spa.html", context={"posts": posts_on_page})

def add_new_message(request):
    if request.method == 'POST':
        post_form = PostForm(request.POST)
        if post_form.is_valid():
            try:
                post_form.save()
                messages.success(request, "Your message was successfully added!")
            
            except ValueError as err:
                messages.error(request, f"ValueError: {err}")
                return render(request, "spa/add_new_messages.html", {"form": post_form})
            
            except Exception as err:
                messages.error(request, f"An unexpected error occurred: {err}")
                return render(request, "spa/add_new_messages.html", {"form": post_form})

            return redirect(to="spa:main_spa")  
    else:
        post_form = PostForm()
    
    return render(request, 'spa/add_new_message.html', {'post_form': post_form})