from rest_framework.generics import get_object_or_404
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from event_feed.models import Note, Advertisement, Achievement, User
from typing import List, Type, Dict
from django.db.models import Model, CharField, Value
from event_feed.serializers import EventFeedSerializer, Entity


def get_event_feed(
        models: List[Type[Model]],
        user_id: int,
        event_type: str,
        search: str
) -> List[Dict]:
    result_list = []

    for model in models:
        entity_name = model.__name__.lower()
        records = model.objects.annotate(
            entity=Value(
                entity_name,
                output_field=CharField()
            )
        ).order_by('-created_at').values('entity', 'id', 'created_at', 'title')

        if entity_name == Entity.Note.value:
            records = records.filter(created_by=user_id)
        elif entity_name == Entity.Achievement.value:
            records = records.filter(users__id=user_id)

        if event_type:
            records = records.filter(entity__in=['advertisement', event_type])
        if search:
            records = records.filter(title__icontains=search)

        result_list += list(records)

    return sorted(result_list, key=lambda x: x['created_at'], reverse=True)


class EventFeedAPIView(APIView):
    permission_classes = [AllowAny]
    serializer_class = EventFeedSerializer
    pagination_class = PageNumberPagination
    queryset = User.objects.exclude(is_staff=True)
    lookup_field = "pk"

    def get(self, request, *args, **kwargs):
        lookup_value = self.kwargs.get(self.lookup_field)
        user = get_object_or_404(
            self.queryset, **{self.lookup_field: lookup_value}
        )

        query = self.request.query_params
        data = get_event_feed(
            models=[Note, Advertisement, Achievement],
            user_id=user.id,
            event_type=query.get("type", ""),
            search=query.get("search", "")
        )
        serializer_data = self.serializer_class(data, many=True).data
        paginator = self.pagination_class()
        paginated = paginator.paginate_queryset(serializer_data, request)
        return paginator.get_paginated_response(paginated)
