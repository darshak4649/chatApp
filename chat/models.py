from django.db import models


class Users(models.Model):
    name = models.CharField(max_length=200)
    phone = models.CharField(max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Chats(models.Model):
    chat = models.CharField(max_length=2000)
    sender_id =  models.CharField(max_length=200)
    user_id = models.ForeignKey(Users, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)