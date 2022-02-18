from django import forms
from .models import Category

class NewsForm(forms.Form):
    title = forms.CharField(max_length=150, label='Название:', widget=forms.TextInput(
        attrs={"class": "form-control"})
    )
    content = forms.CharField(label='Содержимое:', required=False, widget=forms.Textarea(
        attrs={
            "class": "form-control",
            "row": 5
        }
    ))
    is_published = forms.BooleanField(label='Опубликовано?:', initial=True)
    category = forms.ModelChoiceField(label='Категория', empty_label='Выберите категорию', queryset=Category.objects.all(),
                                      widget=forms.Select(
                                          attrs={"class": "form-control"}))
