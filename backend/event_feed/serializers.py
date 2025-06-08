from enum import Enum
from rest_framework import serializers


class Entity(Enum):
    Note = "note"
    Advertisement = "advertisement"
    Achievement = "userachievement"


class EventFeedSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField(source='head')
    entity = serializers.ChoiceField(
        choices=[e.value for e in Entity]
    )
    created_at = serializers.DateTimeField()
