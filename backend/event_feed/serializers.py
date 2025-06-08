from enum import Enum
from rest_framework import serializers


class Entyty(Enum):
    Note = "note"
    Advertisement = "advertisement"
    Achievement = "achievement"


class EventFeedSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField()
    entity = serializers.ChoiceField(
        choices=[e.value for e in Entyty]
    )
    created_at = serializers.DateTimeField()
