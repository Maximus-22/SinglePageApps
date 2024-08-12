from django.forms import ModelForm, TextInput, FileInput, CharField, EmailField, ImageField
from .models import Post, Comment


class PostForm(ModelForm):
    user_name = CharField(required=True, min_length=3, max_length=64, help_text="You can type from 3 to 64 characters")
    email = EmailField(required=True, min_length=8, max_length=128, help_text="You can type from 8 to 128 characters")
    avatar_url = CharField(required=False, min_length=12, max_length=128, help_text="Not necessary (from 8 to 128 characters)")
    # text = CharField(required=True, min_length=3, max_length=64, help_text="Limit to 1028 characters")
    file_data = ImageField(required=False, widget=FileInput(),
                           help_text="Please upload files smaller than 1 MB. Аllowed extensions are .txt, .png, .jpeg, .jpg, .gif")

    class Meta:
        model = Post
        fields = ["user_name", "email", "avatar_url", "text", "file_data"]

    # def clean_tags(self):
    #     # [cleaned_data] -> типу <a box of chocolates> от запроса [POST]
    #     tags = self.cleaned_data['tags']
    #     # Розбиваємо рядок з тегами на список, використовуючи кому як роздільник
    #     return [tag.strip() for tag in tags.split(',')]