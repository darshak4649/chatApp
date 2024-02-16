from django import forms
from .models import Users, Chats


class UsersForm(forms.ModelForm):
    class Meta:
        model = Users
        fields = ['name', 'phone']
        
        
class ChatsForm(forms.ModelForm):
    class Meta:
        model = Chats
        fields = ['chat', 'sender_id', 'user_id']