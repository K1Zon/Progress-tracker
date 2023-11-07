from django.shortcuts import render
from .models import Topic

def index(request):     # Home page for learning_logs app
    return render(request, 'learning_logs/index.html')

def topics(request):
    topics = Topic.objects.order_by('date_added')
    context = {'topics':topics}
    return render(request, 'learning_logs/topics.html', context)
