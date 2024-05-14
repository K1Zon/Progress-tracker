from django.contrib import admin
from .models import Topic, Entry


admin.site.register(Topic)





class EntryAdmin(admin.ModelAdmin):
    list_display = ('id', 'text', 'topic', 'date_added', 'completed')
    list_filter = ('date_added', 'completed')
    search_fields = ('text', 'topic')

admin.site.register(Entry, EntryAdmin)
