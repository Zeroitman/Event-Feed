from enum import Enum
from rest_framework import serializers


class QueryEntity(Enum):
    Note = "note"
    UserAchievement = "userachievement"


class Entity(Enum):
    Note = "note"
    UserAchievement = "userachievement"
    Advertisement = "advertisement"


class EventFeedQueryParamSerializer(serializers.Serializer):
    event_type = serializers.ChoiceField(
        choices=[e.value for e in QueryEntity], required=False
    )
    search = serializers.CharField(required=False)


class EventFeedSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField(source='head')
    entity = serializers.ChoiceField(
        choices=[e.value for e in Entity]
    )
    created_at = serializers.DateTimeField()
