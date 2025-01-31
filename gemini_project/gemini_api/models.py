from urllib import response
from django.db import models
import google.generativeai as genai
from django.conf import settings

# Create your models here.

class Chat(models.Model):
    prompt = models.TextField()
    response = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'gemini_api_chat'

    def __str__(self):
        return f"Chat {self.id}"