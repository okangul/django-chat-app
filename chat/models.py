from django.contrib.auth import get_user_model
from django.db import models
from django_extensions.db.models import TimeStampedModel

User = get_user_model()


class Message(TimeStampedModel):
    author = models.ForeignKey(User, related_name='author_messages', on_delete=models.CASCADE)
    content = models.TextField()

    def __str__(self):
        return self.author.username

    @staticmethod
    def last_10_messages():
        return Message.objects.all().order_by('-created')[:10]
