from django.shortcuts import render, redirect
from .models import Users, Chats
from .forms import UsersForm, ChatsForm
from django.core.exceptions import ObjectDoesNotExist

def chats(request):
    users = Users.objects.all()
    return render(request, 'users.html', {'users': users})

def create_user(request):
    if request.method == 'POST':
        form = UsersForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('chats')
    else:
        form = UsersForm()
    return render(request, 'create_user.html', {'form': form})

def user_chat(request, user_id):
    if request.method == 'POST':
        sender_id = request.POST.get('sender_id')
        chats = ChatsForm(request.POST)
        # print(chats["sender_id"])
        if chats.is_valid():
            chats.save()
            return redirect('user_chat', user_id=sender_id)
    else:
        user = Users.objects.get(id=user_id)
        chats = Chats.objects.all()
        return render(request, 'user_chat.html', {'user': user, 'chats': chats})   

    
