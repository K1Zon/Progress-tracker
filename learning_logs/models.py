from django.db import models
from django.contrib.auth.models import User


class Topic(models.Model):  # Тема пользователя
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        return self.text


class Entry(models.Model): # Данные по теме пользователя
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    completed = models.BooleanField(default=False)


    class Meta:
        verbose_name_plural = 'entries'
        ordering = ['id']

    def __str__(self):
        if len(self.text) < 50:
            return f"{self.text[:50]}"
        else: 
            return f"{self.text[:50]}..."