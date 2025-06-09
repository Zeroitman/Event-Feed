from django import forms
from event_feed.models import UserAchievement, User, Note


class UserAchievementAdminForm(forms.ModelForm):
    class Meta:
        model = UserAchievement
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['user'].queryset = User.objects.filter(is_staff=False)


class UserNoteAdminForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['created_by'].queryset = User.objects.filter(
            is_staff=False
        )
