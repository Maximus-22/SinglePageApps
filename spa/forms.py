from django import forms
from .models import Post, Comment


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ["user_name", "email", "avatar_url", "text"]

    # def clean_tags(self):
    #     # [cleaned_data] -> типу <a box of chocolates> от запроса [POST]
    #     tags = self.cleaned_data['tags']
    #     # Розбиваємо рядок з тегами на список, використовуючи кому як роздільник
    #     return [tag.strip() for tag in tags.split(',')]