from django import forms
from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('author', 'categoryType', 'postCategory', 'title', 'text')

    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)
        self.fields['author'].label = "Автор:"
        self.fields['categoryType'].label = "Тип публикации:"
        self.fields['postCategory'].label = "Категория:"
        self.fields['title'].label = "Название публикации:"
        self.fields['text'].label = "Текст публикации:"