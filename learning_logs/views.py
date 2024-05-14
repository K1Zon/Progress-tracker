from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import Http404
from .models import Topic, Entry
from .forms import TopicForm, EntryForm
from django.http import JsonResponse


@login_required
def toggle_entry_completion(request, entry_id):
    entry = Entry.objects.get(id=entry_id)
    entry.completed = not entry.completed
    entry.save()

    completed_entries_count = entry.topic.entry_set.filter(completed=True).count()
    total_entries_count = entry.topic.entry_set.count()

    completion_percentage = (completed_entries_count / total_entries_count) * 100 if total_entries_count != 0 else 0
    completion_percentage = round(completion_percentage, 2)
    print(completion_percentage)
    return JsonResponse({'message': 'Success', 'completion_percentage': completion_percentage})



def index(request):  # Home page for learning_logs app
    return render(request, 'learning_logs/index.html')

@login_required
def topics(request):
    topics = Topic.objects.filter(owner=request.user).order_by('-date_added')
    context = {'topics': topics}

    return render(request, 'learning_logs/topics.html', context)



@login_required
def topic(request, topic_id):
    topic = Topic.objects.get(id=topic_id)
    check_topic_owner(topic, request)
    entries = topic.entry_set.order_by('id')
    completed_entries_count = topic.entry_set.filter(completed=True).count()
    total_entries_count = topic.entry_set.count()
    completion_percentage = (completed_entries_count / total_entries_count) * 100 if total_entries_count != 0 else 0
    # round(completion_percentage, 2)
    completion_percentage = round(completion_percentage, 2)
    context = {'topic': topic, 'entries': entries, 'completion_percentage': completion_percentage}
    return render(request, 'learning_logs/topic.html', context)


@login_required
def new_topic(request):
    if request.method != 'POST':
        form = TopicForm()
    else:
        form = TopicForm(data=request.POST)
        if form.is_valid():
            new_topic = form.save(commit=False)
            new_topic.owner = request.user
            new_topic.save()

            # Создаем записи для новой темы
            if form.cleaned_data['presets'] == 'weekly':
                num_entries = 7
            elif form.cleaned_data['presets'] == 'monthly':
                num_entries = 30
            # else:
            #     num_entries = 1
            if form.cleaned_data['presets'] == 'weekly' or form.cleaned_data['presets'] == 'monthly':
                for _ in range(num_entries):
                    data = {'text': 'Дeнь ' + str(_ + 1)}
                    entry = Entry(topic=new_topic, text=data['text'])
                    entry.save()
            else:
                pass
            return redirect('learning_logs:topics')

    context = {'form': form}
    return render(request, 'learning_logs/new_topic.html', context)


@login_required
def new_entry(request, topic_id):
    topic = Topic.objects.get(id=topic_id)
    check_topic_owner(topic, request)
    if request.method != 'POST':
        form = EntryForm()
    else:
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.save()
            return redirect('learning_logs:topic', topic_id=topic_id)

    context = {'topic': topic, 'form': form}
    return render(request, 'learning_logs/new_entry.html', context)


@login_required
def edit_entry(request, entry_id):
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic
    check_topic_owner(topic, request)
    if request.method != 'POST':
        form = EntryForm(instance=entry)
    else:
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('learning_logs:topic', topic_id=topic.id)

    context = {'entry': entry, 'topic': topic, 'form': form}
    return render(request, 'learning_logs/edit_entry.html', context)




def check_topic_owner(topic, request):
    if topic.owner != request.user:
        raise Http404