from django import forms
from .models import Message

class MessageForm(forms.Form):
    name = forms.CharField(max_length=200)
    email = forms.EmailField(max_length=254)
    feedback = forms.CharField(
        max_length=2050,
         widget=forms.Textarea(),
        help_text='Write here your message!'
    )

    class Meta:
        model = Message
        fields = (
            'name',
            'email',
            'feedback',
        )
    

    def clean(self):
        cleaned_data = super(MessageForm, self).clean()
        name = cleaned_data.get('name')
        email = cleaned_data.get('email')
        feedback = cleaned_data.get('feedback')
        if not name and not email and not feedback:
            raise forms.ValidationError('You have to write something!')