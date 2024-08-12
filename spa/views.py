from rest_framework import viewsets

from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, redirect, get_object_or_404

from .forms import PostForm
from .models import Post, Comment, File, validate_file_size, upload_file
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
        post_form = PostForm(request.POST, request.FILES, instance=Post())
        """request.FILES містить файли, завантажені через форму з html, і ключем у цьому словнику буде значення,
           вказане в атрибуті [name] тега <input>
        """
        file_size_error = validate_file_size(request.FILES['file_data'])
        file_name = request.FILES['file_data'].name
        file_ext_error = upload_file(None, file_name)

        if file_size_error:
            messages.error(request, file_size_error)
            return render(request, "spa/add_new_message.html", {"form": post_form})

        if file_ext_error.startswith("The extension"):
            messages.error(request, file_ext_error)
            return render(request, "spa/add_new_message.html", {"form": post_form})

        if post_form.is_valid():
            try:
                post = post_form.save()
                messages.success(request, "Your message was successfully added!")
                file = post_form.cleaned_data['file_data']

                if file:
                    file_instance = File(path=file, user_post=post)
                    file_instance.save()
                    messages.success(request, "Your data was successfully saved!")
            
            except ValueError as err:
                messages.error(request, f"ValueError: {err}")
                return render(request, "spa/add_new_message.html", {"form": post_form})
            
            except Exception as err:
                messages.error(request, f"An unexpected error occurred: {err}")
                return render(request, "spa/add_new_message.html", {"form": post_form})

            return redirect(to="spa:main_spa")  
    else:
        post_form = PostForm()
    
    return render(request, 'spa/add_new_message.html', {'post_form': post_form})