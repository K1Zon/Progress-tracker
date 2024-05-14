from django import forms
from .models import Topic, Entry


class TopicForm(forms.ModelForm):
    presets = forms.ChoiceField(choices=(('weekly', 'Недельный'), ('monthly', 'Месячный'), ('daily', 'Ежедневный')), label='Пресет')

    class Meta:
        model = Topic
        fields = ['text', 'presets']
        labels = {'text': 'Тема', 'presets': 'Пресет'}
    

class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['text']
        labels = {'text': 'Запись'}
        widgets = {'text': forms.Textarea(attrs={'cols':80})}
