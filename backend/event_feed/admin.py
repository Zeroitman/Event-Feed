from django.contrib import admin
from event_feed.models import (
    Note, Advertisement, UserAchievement, Achievement, User
)

admin.site.register(User)
admin.site.register(Note)
admin.site.register(Achievement)
admin.site.register(Advertisement)


@admin.register(UserAchievement)
class UserAchievementAdmin(admin.ModelAdmin):
    list_display = ("user", "achievement", "created_at")
    list_filter = ("created_at",)
