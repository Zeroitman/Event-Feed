from django.contrib import admin
from event_feed.models import Note, Achievement, Advertisement, User


admin.site.register(User)
admin.site.register(Note)
admin.site.register(Achievement)
admin.site.register(Advertisement)
