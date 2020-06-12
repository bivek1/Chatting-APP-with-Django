from django import forms
from .models import chat, chat2
class cha(forms.ModelForm):
    class Meta:
        model = chat
        fields = ('id', 'textline')
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['textline'].widget.attrs.update({'class':"textareaforchat",'placeholder':'Write your message here'})

class cha2(forms.ModelForm):
    class Meta:
        model = chat2
        fields = ('id', 'textfie')
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['textfie'].widget.attrs.update({'class':"textareaforchat",'placeholder':'Write your message here'})