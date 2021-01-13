from django.db import models
class User(models.Model):

    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email=models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    #objects = UserManager()
    def __str__(self):
        return f"<Dojo object: {self.first_name+self.last_name} ({self.id})>"

class Message(models.Model):
    title = models.CharField(max_length=255)
    user = models.ForeignKey(User, related_name="messages", on_delete=models.CASCADE)
    message = models.TextField(default="default!")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return f"<Book object: {self.title+self.message} ({self.id})>"

class Comment(models.Model):
    user = models.ForeignKey(User, related_name="comments", on_delete=models.CASCADE)
    message = models.ForeignKey(Message, related_name="comments", on_delete=models.CASCADE)
    comment = models.TextField(default="default!")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return f"<Book object: {self.comment} ({self.id})>"
