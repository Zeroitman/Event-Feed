from django.contrib import admin
from event_feed.form.user_achievement import (
    UserAchievementAdminForm, UserNoteAdminForm
)
from event_feed.models import (
    Note, Advertisement, UserAchievement, Achievement
)

# admin.site.register(User) / Activate if want CRUD users in admin panel


@admin.register(Achievement)
class AchievementAdmin(admin.ModelAdmin):
    list_display = ("title", )


@admin.register(Advertisement)
class AdvertisementAdmin(admin.ModelAdmin):
    list_display = ("title", )


@admin.register(Note)
class UserNoteAdmin(admin.ModelAdmin):
    form = UserNoteAdminForm
    list_display = ("created_by", "title", "created_at")
    list_filter = ("created_at",)


@admin.register(UserAchievement)
class UserAchievementAdmin(admin.ModelAdmin):
    form = UserAchievementAdminForm
    list_display = ("user", "achievement", "created_at")
    list_filter = ("created_at",)
